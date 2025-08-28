## Power Query clean up:
- filter full dataset into France & Germany 1993-2023
- set variables to fitting data types
- add new column: gdp_million_usd
- change all % columns: divide by 100, so later when format as "%" will show correct values

# data quality check:
- no gdp data for 2023 for both countries -> decided to keep 2023 data nevertheless
- overall data completeness 98% -> dataset is analysis-ready

next step:
- make a time series line chart show different energy share per country

# metric relationships:

PRIMARY ENERGY CONSUMPTION

- fossil_share_energy
    - coal_share_energy
    - gas_share_energy
    - oil_share_energy
    
- low_carbon_share_energy
    - renewables_share_energy
        - hydro_share_energy
        - wind_share_energy
        - solar_share_energy
        - biofuel_share_energy
        - other_renewables_share_energy
    - nuclear_share_energy

# learnings
- before starting the analysis, really take the time to understand each metric and their relationships to each other. this can save a lot of hassle later on
- before making beautiful charts, just play around to find insights
