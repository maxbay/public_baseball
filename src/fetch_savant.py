import os
import sys
from pybaseball import statcast
import pandas as pd
import numpy as np
import datetime
import urllib.request
from io import StringIO

class StatcastDataHandler:
    def __init__(self):
        self.type_conversion = {
            'game_pk': int,
            'pitch_type': str,
            'game_date': 'datetime64[ns]',
            'game_year': int,
            'release_speed': float,
            'release_pos_x': float,
            'release_pos_z': float,
            'player_name': str,
            'batter': int,
            'pitcher': int,
            'events': str,
            'description': str,
            'spin_dir': float,
            'zone': str,
            'des': str,
            'game_type': str,
            'stand': str,
            'p_throws': str,
            'home_team': str,
            'away_team': str,
            'type': str,
            'hit_location': float,
            'bb_type': str,
            'balls': int,
            'strikes': int,
            'pfx_x': float,
            'pfx_z': float,
            'plate_x': float,
            'plate_z': float,
            'on_3b': float,
            'on_2b': float,
            'on_1b': float,
            'outs_when_up': int,
            'inning': int,
            'inning_topbot': str,
            'fielder_2': int,
            'fielder_3': int,
            'fielder_4': int,
            'fielder_5': int,
            'fielder_6': int,
            'fielder_7': int,
            'fielder_8': int,
            'fielder_9': int,
            'umpire': float,
            'vx0': float,
            'vy0': float,
            'vz0': float,
            'ax': float,
            'ay': float,
            'az': float,
            'sz_top': float,
            'sz_bot': float,
            'hc_x': float,
            'hc_y': float,
            'hit_distance_sc': float,
            'launch_speed': float,
            'launch_angle': float,
            'effective_speed': float,
            'release_spin_rate': float,
            'spin_axis': float,
            'release_extension': float,
            'release_pos_y': float,
            'estimated_ba_using_speedangle': float,
            'estimated_woba_using_speedangle': float,
            'woba_value': float,
            'woba_denom': float,
            'babip_value': float,
            'iso_value': float,
            'launch_speed_angle': float,
            'at_bat_number': int,
            'pitch_number': int,
            'pitch_name': str,
            'home_score': int,
            'away_score': int,
            'bat_score': int,
            'fld_score': int,
            'post_away_score': int,
            'post_home_score': int,
            'post_bat_score': int,
            'post_fld_score': int,
            'if_fielding_alignment': str,
            'of_fielding_alignment': str,
            'delta_home_win_exp': float,
            'delta_run_exp': float,
            'bat_speed': float,
            'swing_length': float,
        }
        self.keep_cols = list(np.sort(list(self.type_conversion.keys())))

    def get_player_meta(self, path='../data/player_meta.feather', update=False):
        if os.path.exists(path) and not update:
            print('Reading from file...')
            return pd.read_feather(path)
        else:
            print('Writing new file...')
            idx_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
            dfs = []
            for i in idx_lst:
                url = f'https://raw.githubusercontent.com/chadwickbureau/register/master/data/people-{i}.csv'
                print(url)
                with urllib.request.urlopen(url) as response:
                    csv_data = response.read().decode('utf-8')
                    df = pd.read_csv(StringIO(csv_data), low_memory=False, verbose=False)
                    dfs.append(df)
            
            player_df = (
                pd.concat(dfs, ignore_index=True)
                .copy()
                .assign(name_full=lambda x: x['name_first'] + ' ' + x['name_last'])
            )[['key_person', 'key_uuid', 'key_mlbam', 'key_retro', 'key_bbref', 'key_fangraphs', 'name_first', 'name_last', 'name_full']]
            
            player_df = (
                player_df
                .dropna(subset=['key_mlbam'])
                .astype({'key_mlbam': int})
                .reset_index(drop=True)
            )
            
            player_df.to_feather(path)
        
        return player_df
    


    def update_local_sc(self, just_current=True):
        player_df = self.get_player_meta(update=True)
        current_year = datetime.datetime.now().year
        years_list = list(range(2015, current_year + 1))

        if just_current:
            years_list = [current_year]
        
        directory_path = '../data/savant/season_data/'
        os.makedirs(directory_path, exist_ok=True)

        for year in years_list:
            year_path = os.path.join(directory_path, f'{year}.feather')
            
            start_date = f'{year}-02-15'
            end_date = f'{year}-11-15'
            
            new_data = True
            if just_current:
                sc_dat_saved = pd.read_feather(year_path)
                start_date = (max(sc_dat_saved['game_date']) + datetime.timedelta(days=1)).strftime('%Y-%m-%d')


            
            sc_dat_tmp = statcast(start_dt=start_date, end_dt=end_date, verbose=False).reset_index(drop=True)

            if sc_dat_tmp.shape[0] == 0:
                print(f'{year} data are current')
                new_data = False

            sc_dat_tmp = (
                sc_dat_tmp[self.keep_cols]
                .astype(self.type_conversion)
                .merge(player_df[['key_mlbam', 'name_full']].rename(columns={'name_full': 'batter_name', 'key_mlbam': 'batter'}), on='batter', how='left')
                .merge(player_df[['key_mlbam', 'name_full']].rename(columns={'name_full': 'pitcher_name', 'key_mlbam': 'pitcher'}), on='pitcher', how='left')
            )
            
            if just_current and new_data:
                sc_dat_tmp = pd.concat([sc_dat_saved, sc_dat_tmp], axis=0, ignore_index=True).reset_index(drop=True)

            sc_dat_tmp.to_feather(year_path)

    def fetch_statcast(self, start_year=None, end_year=None, game_types=['W', 'L', 'D', 'F', 'R', 'S']):
        if start_year is None and end_year is None:
            Warning('both start_year and end_year not provided, not fetching data')
            exit(1)
        elif end_year is None:
            end_year = datetime.datetime.now().year

        start_year = int(start_year)
        end_year = int(end_year)

        years_list = list(range(start_year, end_year + 1))

        df_list = []
        directory_path = '../data/savant/season_data/'
        print(f'Fetching: {years_list}')
        for year in years_list:
            year_path = os.path.join(directory_path, f'{year}.feather')
            tmp_df = pd.read_feather(year_path)
            tmp_df = tmp_df[tmp_df['game_type'].isin(game_types)]
            df_list.append(tmp_df)

        df = pd.concat(df_list, axis=0, ignore_index=True).reset_index(drop=True)

        return df


