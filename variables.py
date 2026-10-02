def generar_mapa(data, davis):
    def f_to_c(f_val):
        try: return str(round((float(f_val) - 32) * 5 / 9, 1)) + " °C"
        except: return "N/A"

    def mph_to_kmh(mph_val):
        try: return str(round(float(mph_val) * 1.60934, 1)) + " km/h"
        except: return "N/A"

    def in_to_mm(in_val):
        try: return str(round(float(in_val) * 25.4, 1)) + " mm"
        except: return "0.0 mm"

    def in_hr_to_mm_hr(in_val):
        try: return str(round(float(in_val) * 25.4, 1)) + " mm/h"
        except: return "0.0 mm/h"

    def get_raw(val, unit=""):
        return f"{val} {unit}".strip() if val is not None else "N/A"

    return {
        "{{STATION_NAME}}": get_raw(davis.get("station_name"), ""),
        "{{OBS_TIME}}": get_raw(data.get("observation_time"), ""),
        "{{SUNRISE}}": get_raw(davis.get("sunrise"), ""),
        "{{SUNSET}}": get_raw(davis.get("sunset"), ""),
        "{{TEMP_ACT}}": get_raw(data.get("temp_c"), "°C"),
        "{{HUM_ACT}}": get_raw(data.get("relative_humidity"), "%"),
        "{{PRES_ACT}}": get_raw(data.get("pressure_mb"), "hPa"),
        "{{PRES_TEND}}": get_raw(davis.get("pressure_tendency_string"), ""),
        "{{DEW_ACT}}": get_raw(data.get("dewpoint_c"), "°C"),
        "{{WINDCHILL_ACT}}": get_raw(data.get("windchill_c"), "°C"),
        "{{HEATINDEX_ACT}}": get_raw(data.get("heat_index_c"), "°C"),
        "{{WIND_ACT}}": mph_to_kmh(data.get("wind_mph")),
        "{{WIND_DIR}}": get_raw(data.get("wind_dir"), ""),
        "{{WIND_DEG}}": get_raw(data.get("wind_degrees"), "°"),
        "{{WIND_10M_AVG}}": mph_to_kmh(davis.get("wind_ten_min_avg_mph")),
        "{{WIND_10M_GUST}}": mph_to_kmh(davis.get("wind_ten_min_gust_mph")),
        "{{SOLAR_ACT}}": get_raw(davis.get("solar_radiation"), "W/m²"),
        "{{UV_ACT}}": get_raw(davis.get("uv_index"), ""),
        "{{RAIN_RATE_ACT}}": in_hr_to_mm_hr(davis.get("rain_rate_in_per_hr")),
        "{{RAIN_DAY}}": in_to_mm(davis.get("rain_day_in")),
        "{{RAIN_MONTH}}": in_to_mm(davis.get("rain_month_in")),
        "{{RAIN_YEAR}}": in_to_mm(davis.get("rain_year_in")),
        "{{RAIN_STORM}}": in_to_mm(davis.get("rain_storm_in")),
        "{{RAIN_STORM_START}}": get_raw(davis.get("rain_storm_start_date"), ""),
        "{{ET_DAY}}": in_to_mm(davis.get("et_day")),
        "{{ET_MONTH}}": in_to_mm(davis.get("et_month")),
        "{{ET_YEAR}}": in_to_mm(davis.get("et_year")),
        "{{TEMP_DAY_HIGH}}": f_to_c(davis.get("temp_day_high_f")),
        "{{TEMP_DAY_HIGH_TIME}}": get_raw(davis.get("temp_day_high_time")),
        "{{TEMP_DAY_LOW}}": f_to_c(davis.get("temp_day_low_f")),
        "{{TEMP_DAY_LOW_TIME}}": get_raw(davis.get("temp_day_low_time")),
        "{{HUM_DAY_HIGH}}": get_raw(davis.get("relative_humidity_day_high"), "%"),
        "{{HUM_DAY_HIGH_TIME}}": get_raw(davis.get("relative_humidity_day_high_time")),
        "{{HUM_DAY_LOW}}": get_raw(davis.get("relative_humidity_day_low"), "%"),
        "{{HUM_DAY_LOW_TIME}}": get_raw(davis.get("relative_humidity_day_low_time")),
        "{{PRES_DAY_HIGH}}": get_raw(davis.get("pressure_day_high_in"), "inHg"),
        "{{PRES_DAY_HIGH_TIME}}": get_raw(davis.get("pressure_day_high_time")),
        "{{PRES_DAY_LOW}}": get_raw(davis.get("pressure_day_low_in"), "inHg"),
        "{{PRES_DAY_LOW_TIME}}": get_raw(davis.get("pressure_day_low_time")),
        "{{DEW_DAY_HIGH}}": f_to_c(davis.get("dewpoint_day_high_f")),
        "{{DEW_DAY_HIGH_TIME}}": get_raw(davis.get("dewpoint_day_high_time")),
        "{{DEW_DAY_LOW}}": f_to_c(davis.get("dewpoint_day_low_f")),
        "{{DEW_DAY_LOW_TIME}}": get_raw(davis.get("dewpoint_day_low_time")),
        "{{WINDCHILL_DAY_LOW}}": f_to_c(davis.get("windchill_day_low_f")),
        "{{WINDCHILL_DAY_LOW_TIME}}": get_raw(davis.get("windchill_day_low_time")),
        "{{HEATINDEX_DAY_HIGH}}": f_to_c(davis.get("heat_index_day_high_f")),
        "{{HEATINDEX_DAY_HIGH_TIME}}": get_raw(davis.get("heat_index_day_high_time")),
        "{{WIND_DAY_HIGH}}": mph_to_kmh(davis.get("wind_day_high_mph")),
        "{{WIND_DAY_HIGH_TIME}}": get_raw(davis.get("wind_day_high_time")),
        "{{SOLAR_DAY_HIGH}}": get_raw(davis.get("solar_radiation_day_high"), "W/m²"),
        "{{SOLAR_DAY_HIGH_TIME}}": get_raw(davis.get("solar_radiation_day_high_time")),
        "{{UV_DAY_HIGH}}": get_raw(davis.get("uv_index_day_high")),
        "{{UV_DAY_HIGH_TIME}}": get_raw(davis.get("uv_index_day_high_time")),
        "{{RAIN_RATE_DAY_HIGH}}": in_hr_to_mm_hr(davis.get("rain_rate_day_high_in_per_hr")),
        "{{RAIN_RATE_DAY_HIGH_TIME}}": get_raw(davis.get("rain_rate_day_high_time")),
        "{{RAIN_RATE_HR_HIGH}}": in_hr_to_mm_hr(davis.get("rain_rate_hour_high_in_per_hr")),
        "{{TEMP_MON_HIGH}}": f_to_c(davis.get("temp_month_high_f")),
        "{{TEMP_MON_LOW}}": f_to_c(davis.get("temp_month_low_f")),
        "{{HUM_MON_HIGH}}": get_raw(davis.get("relative_humidity_month_high"), "%"),
        "{{HUM_MON_LOW}}": get_raw(davis.get("relative_humidity_month_low"), "%"),
        "{{PRES_MON_HIGH}}": get_raw(davis.get("pressure_month_high_in"), "inHg"),
        "{{PRES_MON_LOW}}": get_raw(davis.get("pressure_month_low_in"), "inHg"),
        "{{DEW_MON_HIGH}}": f_to_c(davis.get("dewpoint_month_high_f")),
        "{{DEW_MON_LOW}}": f_to_c(davis.get("dewpoint_month_low_f")),
        "{{WINDCHILL_MON_LOW}}": f_to_c(davis.get("windchill_month_low_f")),
        "{{HEATINDEX_MON_HIGH}}": f_to_c(davis.get("heat_index_month_high_f")),
        "{{WIND_MON_HIGH}}": mph_to_kmh(davis.get("wind_month_high_mph")),
        "{{SOLAR_MON_HIGH}}": get_raw(davis.get("solar_radiation_month_high"), "W/m²"),
        "{{UV_MON_HIGH}}": get_raw(davis.get("uv_index_month_high")),
        "{{RAIN_RATE_MON_HIGH}}": in_hr_to_mm_hr(davis.get("rain_rate_month_high_in_per_hr")),
        "{{TEMP_YEAR_HIGH}}": f_to_c(davis.get("temp_year_high_f")),
        "{{TEMP_YEAR_LOW}}": f_to_c(davis.get("temp_year_low_f")),
        "{{HUM_YEAR_HIGH}}": get_raw(davis.get("relative_humidity_year_high"), "%"),
        "{{HUM_YEAR_LOW}}": get_raw(davis.get("relative_humidity_year_low"), "%"),
        "{{PRES_YEAR_HIGH}}": get_raw(davis.get("pressure_year_high_in"), "inHg"),
        "{{PRES_YEAR_LOW}}": get_raw(davis.get("pressure_year_low_in"), "inHg"),
        "{{DEW_YEAR_HIGH}}": f_to_c(davis.get("dewpoint_year_high_f")),
        "{{DEW_YEAR_LOW}}": f_to_c(davis.get("dewpoint_year_low_f")),
        "{{WINDCHILL_YEAR_LOW}}": f_to_c(davis.get("windchill_year_low_f")),
        "{{HEATINDEX_YEAR_HIGH}}": f_to_c(davis.get("heat_index_year_high_f")),
        "{{WIND_YEAR_HIGH}}": mph_to_kmh(davis.get("wind_year_high_mph")),
        "{{SOLAR_YEAR_HIGH}}": get_raw(davis.get("solar_radiation_year_high"), "W/m²"),
        "{{UV_YEAR_HIGH}}": get_raw(davis.get("uv_index_year_high")),
        "{{RAIN_RATE_YEAR_HIGH}}": in_hr_to_mm_hr(davis.get("rain_rate_year_high_in_per_hr")),
    }
