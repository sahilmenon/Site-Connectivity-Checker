# Site Connectivity Checker
 A simple Python application is a simple utility to check if a connection can be established to a given URL. It utilizes the http.client module to make a HEAD request to the specified URL on both port 80 and port 443, indicating successful connection if either port responds without error.

This project was done by me many years ago when I was first learning Python. This project may seem simple but has various essential concepts such as:

* Networking
* URL Parsing
* String Formatting
* Error Handling
* Flow Control
* Functions
* Console Output

## Usage
To use the connectioned function, import it into your Python script and call it with the desired URL. Optionally, you can specify a timeout duration for the connection attempt.

    from connectioned import connectioned

    url = "https://example.com"
    timeout = 5

    try:
        if connectioned(url, timeout):
            print("Connection successful!")
        else:
            print("Connection failed.")
    except Exception as e:
        print(f"An error occurred: {e}")

## Parameters
url: The URL to check for a successful connection.

timeout (optional): The timeout duration for the connection attempt in seconds. Default is 5 seconds.


## Exceptions
If an error occurs during the connection attempt, an exception will be raised. The exception contains details about the error encountered.


    import connectioned

    url = "https://www.google.com"

    try:
        if connectioned(url):
            print("Connection successful!")
        else:
            print("Connection failed.")
    except Exception as e:
        print(f"An error occurred: {e}")


## Watch the demo:
TBD

## Dependencies
This code requires Python and only uses The Python Standard Library.

## Issues and Contributions
If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.

Happy coding!
