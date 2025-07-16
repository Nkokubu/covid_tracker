import requests
import matplotlib.pyplot as plt

def fetch_covid_data(country: str, days: int = 30):
    """Fetch COVID-19 historical data from disease.sh API."""
    url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays={days}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    
    data = response.json()
    cases = data['timeline']['cases']
    return cases

def plot_cases(cases: dict, country: str):
    """Plot COVID-19 case trends."""
    dates = list(cases.keys())
    case_counts = list(cases.values())

    # Convert cumulative cases to daily new cases
    new_cases = [case_counts[0]] + [case_counts[i] - case_counts[i-1] for i in range(1, len(case_counts))]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, new_cases, marker='o', linestyle='-', color='blue')
    plt.xticks(rotation=45)
    plt.title(f"Daily New COVID-19 Cases in {country}")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    country = input("Enter a country name (e.g., USA, Canada, India): ").strip()
    try:
        covid_cases = fetch_covid_data(country)
        plot_cases(covid_cases, country)
    except Exception as e:
        print(f"Failed to fetch or plot data: {e}")
