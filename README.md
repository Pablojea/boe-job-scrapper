# boe-job-scrapper
Parses Spanish BOE to collect public administration job vacancies based on preference parameters

single_day_mode: If single_day_mode is set to True, will collect data from yesterday BOE.
If single_day_mode is set to False, will parse the number of days provided in timespan variable

time_span : Is the number of days to collect data from

area : Is the name of the province to search offers in. Must be provided in the format '(province_name')