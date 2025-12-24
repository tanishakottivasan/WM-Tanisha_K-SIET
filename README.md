# Smart Waste Bin Network  - Tanisha K
## Virtual IoT Design Challenge


## Project Overview

This project presents a conceptual design of a Smart Waste Bin Network using Internet of Things (IoT) principles to improve urban waste collection efficiency.

The core idea is to enable waste bins to report their fill levels in real time so that garbage collection is performed only when required, instead of following fixed schedules. The design focuses on scalability, low power consumption, and practical city wide deployment rather than complex or expensive hardware.


## Problem Statement

Traditional waste collection systems in cities face several issues:

- Garbage trucks follow fixed routes and schedules
- Some bins overflow while others remain partially empty
- This results in poor hygiene, fuel wastage, and higher operational costs

The primary problem is the absence of real-time visibility into the status of waste bins.


## Proposed Solution

The proposed system introduces an IoT based waste monitoring network where:

- Each waste bin is equipped with basic sensors and a low power microcontroller
- The bin periodically measures its fill level
- Data is transmitted wirelessly to a centralized cloud platform
- City authorities monitor bin status and plan optimized collection routes using a dashboard

System intelligence is centralized in the cloud, while individual bins remain simple, reliable, and energy efficient.


## System Architecture

The system is organized into four main layers:

### Smart Waste Bin (Edge Node)
- Ultrasonic sensor for fill level measurement
- Temperature sensor for fire detection
- ESP32 microcontroller with LoRa communication
- Battery powered with optional solar charging

### Communication Layer
- LoRaWAN used for long range, low power data transmission
- A gateway collects data from multiple bins

### Cloud Platform
- MQTT broker for data ingestion
- Backend services for data processing and storage
- Route optimization logic

### City Operations Dashboard
- Map-based visualization of bin locations
- Color-coded bin status
- Alerts and optimized garbage truck routes

Architecture diagrams are available in the `Software_Architecture` and `Hardware_Architecture` folders.


## Data Flow

The data flow in the system follows these steps:

- Sensor measures the distance to the waste surface
- ESP32 converts the distance into a fill percentage
- Data is transmitted using LoRaWAN
- Gateway forwards data to the cloud platform
- MQTT broker routes data to backend services
- Dashboard updates bin status in real time

MQTT is selected due to its lightweight nature and suitability for low power IoT devices.


## Route Optimization Logic

Garbage collection decisions are based on bin fill levels:

- Bins above 80% fill level are marked for collection
- Priority bins are grouped by operational zones
- The shortest collection route is generated for each zone

This approach minimizes fuel usage and avoids unnecessary pickups.


## Power Management Strategy

To extend battery life:

- Sensor readings are taken every 30 to 60 minutes
- ESP32 operates mostly in deep sleep mode
- Data is transmitted only when thresholds are crossed
- LoRaWAN is used for low energy communication

Expected battery life:
- 6 to 12 months without solar charging
- 12 to 24 months with solar trickle charging

## Reliability and Fault Handling

Basic fault tolerance mechanisms include:

- Multiple sensor readings with median filtering to reduce false values
- Detection of inactive bins if no data is received for 24 hours
- Battery voltage monitoring with low power alerts


## Scalability Considerations

The system is designed for large scale deployment:

- Star topology using LoRaWAN
- One gateway can support hundreds of bins
- Additional gateways can be deployed per city zone
- Cloud services scale automatically with increased load

Mesh networking is avoided due to higher power consumption and added complexity.


## Folder Structure

```text
Smart-Waste-Bin-Network---Tanisha-K/
├── Software/
│   ├── Codes/
│   └── Software_Architecture/
│
├── Hardware/
│   ├── Codes/
│   └── Hardware_Architecture/
│
└── README.md
```

## Assumptions and Limitations

- This project represents a conceptual design, not a full deployment
- Real-world routing would require live map and traffic data
- Sensor accuracy may vary due to environmental conditions


## Future Enhancements

- Predictive fill level estimation using historical data
- Integration with traffic information for smarter routing
- Mobile application support for drivers and maintenance teams


## Final Note

This project emphasizes system level design, feasibility, and scalability. The focus is on solving real urban waste management problems through thoughtful architecture rather than overengineering hardware or software components.
