CREATE TABLE IF NOT EXISTS csse_covid_19_daily_reports_v1(
    `Province/State` STRING,
    `Country/Region` STRING,
    `Last Update` STRING,
    Confirmed STRING,
    Deaths STRING,
    Recovered STRING
);

CREATE TABLE IF NOT EXISTS csse_covid_19_daily_reports_v2(
    `Province/State` STRING,
    `Country/Region` STRING,
    `Last Update` STRING,
    Confirmed STRING,
    Deaths STRING,
    Recovered STRING,
    Latitude STRING,
    Longitude STRING
);

CREATE TABLE IF NOT EXISTS csse_covid_19_daily_reports_v3(
    FIPS STRING,
    Admin2 STRING,
    Province_State STRING,
    Country_Region STRING,
    Last_Update STRING,
    Lat STRING,
    Long_ STRING,
    Confirmed STRING,
    Deaths STRING,
    Recovered STRING,
    Active STRING,
    Combined_Key STRING
)
