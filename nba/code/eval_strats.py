import json

import numpy as np
import pandas as pd

strats = [
		  'Ceiling_1_tbigs', 'Points_1_tbigs', 'CP_1_tbigs', 'CF_1_tbigs', 'PF_1_tbigs', 
		  'Ceiling_2_tbigs', 'Points_2_tbigs', 'CP_2_tbigs', 'CF_2_tbigs', 'PF_2_tbigs', 
		  'Ceiling_3_tbigs', 'Points_3_tbigs', 'CP_3_tbigs', 'CF_3_tbigs', 'PF_3_tbigs', 
		  'Ceiling_4_tbigs', 'Points_4_tbigs', 'CP_4_tbigs', 'CF_4_tbigs', 'PF_4_tbigs', 
		  'Ceiling_5_tbigs', 'Points_5_tbigs', 'CP_5_tbigs', 'CF_5_tbigs', 'PF_5_tbigs', 
		  'Ceiling_6_tbigs', 'Points_6_tbigs', 'CP_6_tbigs', 'CF_6_tbigs', 'PF_6_tbigs', 
		  'Ceiling_7_tbigs', 'Points_7_tbigs', 'CP_7_tbigs', 'CF_7_tbigs', 'PF_7_tbigs',
		  'Ceiling_1_tmeds', 'Points_1_tmeds', 'CP_1_tmeds', 'CF_1_tmeds', 'PF_1_tmeds', 
		  'Ceiling_2_tmeds', 'Points_2_tmeds', 'CP_2_tmeds', 'CF_2_tmeds', 'PF_2_tmeds', 
		  'Ceiling_3_tmeds', 'Points_3_tmeds', 'CP_3_tmeds', 'CF_3_tmeds', 'PF_3_tmeds',
		  'Ceiling_4_tmeds', 'Points_4_tmeds', 'CP_4_tmeds', 'CF_4_tmeds', 'PF_4_tmeds', 
		  'Ceiling_5_tmeds', 'Points_5_tmeds', 'CP_5_tmeds', 'CF_5_tmeds', 'PF_5_tmeds', 
		  'Ceiling_6_tmeds', 'Points_6_tmeds', 'CP_6_tmeds', 'CF_6_tmeds', 'PF_6_tmeds', 
		  'Ceiling_7_tmeds', 'Points_7_tmeds', 'CP_7_tmeds', 'CF_7_tmeds', 'PF_7_tmeds',
		  'Ceiling_1_tsmls', 'Points_1_tsmls', 'CP_1_tsmls', 'CF_1_tsmls', 'PF_1_tsmls', 
		  'Ceiling_2_tsmls', 'Points_2_tsmls', 'CP_2_tsmls', 'CF_2_tsmls', 'PF_2_tsmls', 
		  'Ceiling_3_tsmls', 'Points_3_tsmls', 'CP_3_tsmls', 'CF_3_tsmls', 'PF_3_tsmls',
		  'Ceiling_4_tsmls', 'Points_4_tsmls', 'CP_4_tsmls', 'CF_4_tsmls', 'PF_4_tsmls', 
		  'Ceiling_5_tsmls', 'Points_5_tsmls', 'CP_5_tsmls', 'CF_5_tsmls', 'PF_5_tsmls', 
		  'Ceiling_6_tsmls', 'Points_6_tsmls', 'CP_6_tsmls', 'CF_6_tsmls', 'PF_6_tsmls', 
		  'Ceiling_7_tsmls', 'Points_7_tsmls', 'CP_7_tsmls', 'CF_7_tsmls', 'PF_7_tsmls',
		  ]


strats = ['tbigs_pg', 'tbigs_nopg']#, 'tmeds_pg', 'tmeds_nopg', 'tsmls_pg', 'tsmls_nopg']

strats = ['Points_6_tbigs', 'Points_6_tbigs_pg']

strats = ['asdf', 'asdf_pg', 'asdf_pf', 'asdf_dg', 'asdf_lt', 'asdf_pc',
		  'asdf_lt2', 'asdf_nlt2', 'asdf_npc', 'asdf_npc_dg', 'asdf_wa',
		  'asdf_ceil', 'asdf_ceilo', 'asdf_ceil4', 'asdf_ceil7', 'asdf_ceil7o',
		  'asdf_wa7', 'asdf_wa6o', 'asdf_wa7o']

#strats = ['Ceiling_4_tbigs', 'Points_4_tbigs', 'Floor_4_tbigs']

strats = ['Ceiling_4_tmeds', 'Points_4_tmeds', 'Floor_4_tmeds',
	 	  'Ceiling_4_tsmls', 'Points_4_tmeds']

strats = ['meds_p7', 'meds_c7', 'meds_w7', 'meds_p6', 'meds_c6', 'meds_w6',
 		  'meds_p5', 'meds_c5', 'meds_w5', 'meds_p4', 'meds_c4', 'meds_w4']

strats = ['waforgood', 'wa_fn3', 'wa_fn5']

def eval_all_strats():
	sdf = pd.DataFrame(columns=['cash','gpp', 'gpp_1.1x', 'gpp_1.2x', 'gpp_1.3x', 'tot', 'supertot'])#, 'std'])
	for strat in strats:
		eval_strat(strat, sdf)
	sdf.to_csv('smls.csv')


def eval_strat(strat, sdf):
	df = pd.read_csv('strats/{}.csv'.format(strat))
	cash, gpp = get_lines(df)
	cols = list(df)
	cashes = 0
	gpps = 0
	gpp_11x = 0
	gpp_12x = 0
	gpp_13x = 0
	totc = 0
	totg = 0
	suptot = 0
	#vr = 0
	for i in range(1, len(cols)):
		#vr += np.var(df[df.columns[i]].tolist())
		if not np.isnan(cash[i]):
			cashes += len([a for a in df[df.columns[i]].tolist() if a > cash[i]])
			totc += len([a for a in df[df.columns[i]].tolist() if a > 100])
		

		if not np.isnan(gpp[i]):
			gpps += len([a for a in df[df.columns[i]].tolist() if a > gpp[i]])
			gpp_11x += len([a for a in df[df.columns[i]].tolist() if a > gpp[i]*1.1])
			gpp_12x += len([a for a in df[df.columns[i]].tolist() if a > gpp[i]*1.2])
			gpp_13x += len([a for a in df[df.columns[i]].tolist() if a > gpp[i]*1.3])
			totg += len([a for a in df[df.columns[i]].tolist() if a > 100])
		
		suptot += len([a for a in df[df.columns[i]].tolist()])
	
	fcash = (cashes/totc)*100 if (cashes != 0 and totc != 0) else np.nan
	fgpp = (gpps/totg)*100 if (gpps != 0 and totg != 0) else np.nan
	fgpp_11x = (gpp_11x/totg)*100 if (gpps != 0 and totg != 0) else np.nan
	fgpp_12x = (gpp_12x/totg)*100 if (gpps != 0 and totg != 0) else np.nan
	fgpp_13x = (gpp_13x/totg)*100 if (gpps != 0 and totg != 0) else np.nan	
	ftot = totg if totg != 0 else np.nan

	sdf.loc[strat] = [fcash, fgpp, fgpp_11x, fgpp_12x, fgpp_13x, ftot, suptot,]# np.sqrt(vr)]


def get_lines(df):
	cash = ['cash']
	gpp = ['gpp']
	cols = list(df)
	for i in range(1, len(cols)):
		info = cols[i].split(':')
		info[1] = info[1].replace('teams_', '').replace('.csv', '')

		js = json.loads(open('backtesting_data/{}/cash_stats.json'.format(info[0])).read())[info[1]]

		if 'cash' in js:
			cash.append(js['cash'])
		else:
			cash.append(np.nan)

		if 'gpp' in js:
			gpp.append(js['gpp'])
		else:
			gpp.append(np.nan)

	return cash, gpp

eval_all_strats()

