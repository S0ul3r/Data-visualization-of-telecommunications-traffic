## import of needed values
import matplotlib.pyplot as plt
import pandas as pd

# read data from txt files
data_serviceTimes = pd.read_csv("data/Service_times.txt", sep=" ")
data_serviceTimes.columns = ["Connection time"]
data_callIntensity = pd.read_csv("data/Call_intensity.txt", sep="\t", skip_blank_lines=True)
data_callIntensity.columns = ["Time_unit", "Number_of_submissions"]


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
plt.hist(avgTrafficIntensity["Number_of_submissions"], density=1, facecolor='b', alpha=0.75, bins=12)
plt.title("Histogram najczęściej występujących wartości natężeń")
plt.xlabel("Natężenie ruchu A")
plt.ylabel("Częstość występowania")
plt.xlim(0, 0.35)
plt.grid(True)

plt.show()