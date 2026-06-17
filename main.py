import pandas as pd   #1
file = pd.read_excel("telemetry_data.xlsx")   #2

values = (
    file.groupby("turbine_id")   #3
      .agg(
          average_temp=("temperature_c", "mean"),   #4
          max_vib=("vibration_mm_s", "max")   #5
      )
)

failing_turbine = values[   #6
    (values["average_temp"] > 85.0) |
    (values["max_vib"] > 15.0)   #7
]

print("Failing turbines:")
for turbine_id in failing_turbine.index:   #8
    print(turbine_id)
