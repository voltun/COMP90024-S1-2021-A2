import csv
import json
import pandas as pd

aurinFile = open("aurin-data.txt", "r")
aurinFileLoad = json.loads(aurinFile.read())

aurinHead = aurinFileLoad["wfs:FeatureCollection"]['gml:featureMembers']["aurin:datasource-AU_Govt_ABS_Census-UoM_AURIN_DB_2_lga_i16_lbr_frc_sts_age_sx_abr_trs_str_isl_pers_census_2016"]

# Obtain the dictionary between LGA_CODE and LGA_NAME
df = pd.read_csv(r"AUS_LGA_2016.csv", index_col=0)
df.sort_values(by=['LGA_CODE_2016', "LGA_NAME_2016"], inplace=True)
df.drop_duplicates(subset=['LGA_CODE_2016', "LGA_NAME_2016"], inplace=True)
df.to_csv("LGA_dict.csv")
reader = csv.DictReader(open('LGA_dict.csv'))
LGA_dict = {}
for row in reader:
    LGA_dict[row['LGA_CODE_2016']] = row['LGA_NAME_2016']


# with open("test.csv", 'w', encoding="gbk", newline='') as LGA_dict:
#     field_order = ["LGA_CODE_2016", 'LGA_NAME']
#     writer = csv.DictWriter(LGA_dict, field_order)
#     writer.writeheader()
#     for j in range(0, len(lgaCode)):
#         writer.writerow(dict(zip(field_order, [lgaCode[j], lgaName[j]])))
#
#
jsontext = {"statistic": []}


for index in aurinHead:
    cityName = LGA_dict.get(index["aurin:lga_code16"])
    ageless25 = int(index["aurin:m_emp_worked_ft_a_15_24_y"]) + int(index["aurin:m_emp_worked_pt_a_15_24_y"]) + int(index["aurin:m_eafw_a_15_24_y"]) \
                + int(index["aurin:m_emp_tot_age_15_24_y"]) + int(index["aurin:m_unemp_a_15_24_y"]) + int(index["aurin:m_tot_lf_ag_15_24_y"]) \
                + int(index["aurin:m_not_in_lf_age_15_24_y"]) + int(index["aurin:m_lf_stat_ns_a_15_24_y"]) + int(index["aurin:m_tot_age_15_24_y"]) \
                + int(index["aurin:f_emp_worked_ft_age_15_24_y"]) + int(index["aurin:f_emp_worked_pt_age_15_24_y"]) + int(index["aurin:f_eafw_a_15_24_y"]) \
                + int(index["aurin:f_emp_tot_a_15_24_y"]) + int(index["aurin:f_unemp_a_15_24_y"]) + int(index["aurin:f_tot_lf_a_15_24_y"]) \
                + int(index["aurin:f_not_in_lf_a_15_24_y"]) + int(index["aurin:f_lf_stat_ns_a_15_24_y"]) + int(index["aurin:f_tot_a_15_24_y"]) \
                + int(index["aurin:p_emp_worked_ft_a_15_24_y"]) + int(index["aurin:p_emp_worked_pt_a_15_24_y"]) + int(index["aurin:p_emp_awa_fr_wk_a_15_24_y"]) \
                + int(index["aurin:p_emp_tot_a_15_24_y"]) + int(index["aurin:p_unemp_a_15_24_y"]) + int(index["aurin:p_tot_lf_ag_15_24_y"]) \
                + int(index["aurin:p_not_in_lf_age_15_24_y"]) + int(index["aurin:p_lf_stat_ns_a_15_24_y"]) + int(index["aurin:p_tot_age_15_24_y"])

    total_num = int(index["aurin:m_emp_worked_ft_tot"]) + int(index["aurin:m_emp_worked_pt_tot"]) + int(index["aurin:m_eafw_tot"]) \
                + int(index["aurin:m_emp_tot_tot"]) + int(index["aurin:m_unemp_tot"]) + int(index["aurin:m_tot_lf_tot"]) \
                + int(index["aurin:m_not_in_lf_tot"]) + int(index["aurin:m_lf_status_ns_tot"]) + int(index["aurin:m_tot_tot"]) \
                + int(index["aurin:f_emp_worked_ft_tot"]) + int(index["aurin:f_emp_worked_pt_tot"]) + int(index["aurin:f_eafw_tot"]) \
                + int(index["aurin:f_emp_tot_tot"]) + int(index["aurin:f_unemp_tot"]) + int(index["aurin:f_tot_lf_tot"]) \
                + int(index["aurin:f_not_in_lf_tot"]) + int(index["aurin:f_lf_status_ns_tot"]) + int(index["aurin:f_tot_tot"]) \
                + int(index["aurin:p_emp_worked_ft_tot"]) + int(index["aurin:p_emp_worked_pt_tot"]) + int(index["aurin:p_emp_awa_frop_wk_tot"]) \
                + int(index["aurin:p_emp_tot_tot"]) + int(index["aurin:p_unemp_tot"]) + int(index["aurin:p_tot_lf_tot"]) \
                + int(index["aurin:p_not_in_lf_tot"]) + int(index["aurin:p_lf_status_ns_tot"]) + int(index["aurin:p_tot_tot"])

    jsontext["statistic"].append({"city": cityName, "agelessthan25": ageless25, "totalnum": total_num})

jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '))

f = open('aurin_statistic.json', 'w')
f.write(jsondata)
f.close()

print("success")