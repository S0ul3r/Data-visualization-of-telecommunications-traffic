## import of needed values
import matplotlib.pyplot as plt
import pandas as pd

# read data from txt files
data_serviceTimes = pd.read_csv("data/Service_times.txt", sep=" ")
data_serviceTimes.columns = ["Connection time"]
data_callIntensity = pd.read_csv("data/Call_intensity.txt", sep="\t", skip_blank_lines=True)
data_callIntensity.columns = ["Time_unit", "Number_of_submissions"]
sorted_data_serviceTimes = data_serviceTimes.sort_values(by=['Connection time'], ascending = True)
sorted_data_serviceTimes.insert(0, "ID", range(1, len(sorted_data_serviceTimes)+1))
#sorted_data_serviceTimes = sorted_data_serviceTimes.reset_index()

print(sorted_data_serviceTimes)

# Calculate average service time
avgServiceTime = data_serviceTimes.sum()/len(data_serviceTimes)
# New dict where we will store new values (Traffic intensity)
avgTrafficIntensity = data_callIntensity
# Calculate Traffic intensity (A = TrafficIntensity * avgServiceTime)
avgTrafficIntensity["Number_of_submissions"] = avgTrafficIntensity["Number_of_submissions"] * float(avgServiceTime)
avgTrafficIntensity["Time_unit"] = avgTrafficIntensity["Time_unit"] / 60

# Create a plot of Traffic intensity
plt.subplot(121)
#avgTrafficIntensity.plot(x = "Time_unit", y = "Number_of_submissions", label = "Natężenie", lw=0.8)
plt.plot(avgTrafficIntensity["Time_unit"], avgTrafficIntensity["Number_of_submissions"], label = "Natężenie", lw=0.8)
plt.title("Średnie natężenie ruchu - A = λ * h \nλ - Średnia liczba zgłoszeń na minutę\nh - Średni czas trwania połączenia")
plt.xlabel("Czas [h]")
plt.ylabel("Natężenie ruchu A")
plt.xlim(0, 24)
plt.ylim(0, 0.35)
plt.grid(True)



plt.subplot(122)
#hist = avgTrafficIntensity["Number_of_submissions"].hist(bins=12)
plt.hist(sorted_data_serviceTimes["Connection time"], density=1, facecolor='b', alpha=0.75, bins = 50)
#plt.plot(sorted_data_serviceTimes["ID"], sorted_data_serviceTimes["Connection time"], label = "Natężenie")
plt.title("Histogram czasów połączeń")
plt.xlabel("Czas połączenia")
plt.ylabel("Prawdopodobieństwo")
plt.xlim(0, 1000)
plt.ylim(0, 0.0055)
plt.grid(True)

plt.show()