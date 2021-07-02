Energy saved from recycling
Did you know that recycling saves energy by reducing or eliminating the need to make materials from scratch? For example, aluminum can manufacturers can skip the energy-costly process of producing aluminum from ore by cleaning and melting recycled cans. Aluminum is classified as a non-ferrous metal.

Singapore has an ambitious goal of becoming a zero-waste nation. The amount of waste disposed of in Singapore has increased seven-fold over the last 40 years. At this rate, Semakau Landfill, Singapore’s only landfill, will run out of space by 2035. Making matters worse, Singapore has limited land for building new incineration plants or landfills.

The government would like to motivate citizens by sharing the total energy that the combined recycling efforts have saved every year. They have asked you to help them.

You have been provided with three datasets. The data come from different teams, so the names of waste types may differ.


datasets/wastestats.csv - Recycling statistics per waste type for the period 2003 to 2017
Source: Singapore National Environment Agency
waste_type: The type of waste recycled.
waste_disposed_of_tonne: The amount of waste that could not be recycled (in metric tonnes).
total_waste_recycle_tonne: The amount of waste that could be recycled (in metric tonnes).
total_waste_generated: The total amount of waste collected before recycling (in metric tonnes).
recycling_rate: The amount of waste recycled per tonne of waste generated.
year: The recycling year.
datasets/2018_2019_waste.csv - Recycling statistics per waste type for the period 2018 to 2019
Source: Singapore National Environment Agency
Waste Type: The type of waste recycled.
Total Generated: The total amount of waste collected before recycling (in thousands of metric tonnes).
Total Recycled: The amount of waste that could be recycled. (in thousands of metric tonnes).
Year: The recycling year.
datasets/energy_saved.csv - Estimations of the amount of energy saved per waste type in kWh
material: The type of waste recycled.
energy_saved: An estimate of the energy saved (in kiloWatt hour) by recycling a metric tonne of waste.
crude_oil_saved: An estimate of the number of barrels of oil saved by recycling a metric tonne of waste.




Instructions
The Singapore government has asked you to help them determine how much energy they have saved per year by recycling. You need to answer the following question:

How much energy in kiloWatt hour (kWh) has Singapore saved per year by recycling glass, plastic, ferrous, and non-ferrous metals between 2015 and 2019?

Save your answer as a DataFrame named annual_energy_savings with the an index labelled year. Your DataFrame should consist of one column, total_energy_saved, which contains the total amount of energy in kWh saved per year across the four materials described above. It should resemble the following table:

total_energy_saved
year	
2015	xxxx
2016	xxxx
2017	xxxx
2018	xxxx
2019	xxxx
Note: Unlike the Guided and Unguided Projects that exist on our platform, if you get stuck in this task, you will not have access to any hints, nor will you be able to request a solution. Similarly, our testing process is focused on your answers and will not provide feedback to help you towards your solution. All steps required, including importing, exploration, cleaning, and analysis, will be up to you!
