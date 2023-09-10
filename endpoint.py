from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_data():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if the required parameters are present
    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'}), 400
    
     # Get the current UTC time
    current_time_utc = datetime.datetime.now(datetime.timezone.utc)

    # Calculate the current day of the week (0 = Monday, 6 = Sunday)
    current_day_index = current_time_utc.weekday()

    # Define a list of day names
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Get the current day name based on the index
    current_day = day_names[current_day_index]


    # Get the current day of the week
    #current_day = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone('Etc/GMT-2')).strftime('%A')

    # Get the current UTC time with validation of +/-2 hours
    #current_time_utc = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone('Etc/GMT-2')).strftime('%Y-%m-%d %H:%M:%S')

    # Construct the file URL based on the track
    github_repo_url = "https://github.com/yourusername/yourrepo"
    file_url = f"{github_repo_url}/blob/master/{track}.py"

    # Replace these values with your actual information
    source_code_url = github_repo_url
    status_code = 200

    # Create the response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': track,
        'file_url': file_url,
        'source_code_url': source_code_url,
        'status_code': status_code
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
