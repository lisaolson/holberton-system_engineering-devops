# Load Balancer
The goal for this project was to implement multiple servers that are managed by a load balancer

### Requirements
- Configure Nginx so that its HTTP response contains a custom header
- Configure HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02

### File Descriptions
| File | Description |
| ------------- |:-------------:|
| 0-custom_http_response-header | Double the number of webservers |
| 1-install_load_balancer | Install the load balancer |

#### Author
Lisa Olson
