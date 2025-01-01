import re
from collections import defaultdict
import matplotlib.pyplot as plt


file_path = "/Users/mac/Desktop/CODES/Python/roadmap/server_logs.txt"

def load_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")





def parse_log_entry(line):
    # Example regex for log parsing
    pattern = r"\[(.*?)\] (\w+) (\S+)  (.*)"  # Update this regex if needed
    match = re.match(pattern, line)
    if match:
        timestamp, log_level, user, message = match.groups()
        return {"timestamp": timestamp, "log_level": log_level, "user": user, "message": message}
    return None

def aggregate_data(log_entries):
    error_count = defaultdict(int)
    user_activity = defaultdict(int)
    timestamps = []

    for entry in log_entries:
        if entry["log_level"] == "ERROR":
            error_count[entry["message"]] += 1
        user_activity[entry["user"]] += 1
        timestamps.append(entry["timestamp"])  # Corrected variable name

    return error_count, user_activity, timestamps



def generate_reports(error_count, user_activity, timestamps):
    print("ERROR FREQUENCIES:")
    for error, count in error_count.items():
        print("{}: {} times".format(error, count))

    print("\nUser Activity:")
    for user, activity in user_activity.items():
        print("{}: {} actions".format(user, activity))

    print("\nTimestamps:")
    print(f"Total log entries: {len(timestamps)}")
    print(f"First entry : {min(timestamps)}")
    print(f"Last entry: {max(timestamps)}")


def analyze_log_file(file_path):
    log_entries =[]
    for line in load_log_file(file_path):
        entry = parse_log_entry(line)
        if entry:
            log_entries.append(entry)

    error_count, user_activity, timestamps = aggregate_data(log_entries)
    generate_reports(error_count, user_activity, timestamps)



def plot_error_freq(error_count):
    errors = list(error_count.keys())
    frequencies = list(error_count.values())


    plt.bar(errors, frequencies, color ='red')
    plt.xlabel('Error Types')
    plt.ylabel('Frequency')
    plt.title('Error Frequencies in Logs')
    plt.xticks(rotation=45, ha='right')
    plt.show()




def run_log_analyzer(file_path):
    """
    Implements the entire log analysis process:
    1. Reads the log file.
    2. Parses the log entries.
    3. Aggregates the parsed data.
    4. Generates textual reports.
    5. Visualizes error frequencies using a bar chart.
    """
    # Step 1: Read and parse log file
    log_entries = []
    for line in load_log_file(file_path):
        entry = parse_log_entry(line)
        if entry:
            log_entries.append(entry)

    if not log_entries:
        print("No valid log entries found. Exiting.")
        return

    # Step 2: Aggregate data
    error_count, user_activity, timestamps = aggregate_data(log_entries)

    # Step 3: Generate textual reports
    generate_reports(error_count, user_activity, timestamps)

    # Step 4: Plot error frequencies
    if error_count:
        plot_error_freq(error_count)
    else:
        print("No errors found. Skipping visualization.")



# Provide the path to your log file
file_path = "/Users/mac/Desktop/CODES/Python/roadmap/server_logs.txt"

# Run the log analyzer
run_log_analyzer(file_path)
