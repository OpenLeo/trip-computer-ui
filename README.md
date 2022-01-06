# Trip Computer UI

![preview image](.github/preview.jpg?raw=true)

## Warning

This is one of the first prototypes made, and it's code is quite messy, it does work, but don't count on it being reliable. It is also missing many features (audio panels, previous trips, telematics, phone, climate control...)

## Intro

This is a UI that is meant to be launched alongside the head unit UI and provide a secondary information screen, mostly to display the trip computer (with space to be used for things like navigation and audio informations). It was designed to replace the EMF on cars that can host the RT3/RT4 7" screen

## Integration

It is designed to run on a 7" 1024x600 display, as shown on the preview, but it should run on most other resolutions. It uses socketcan to read the can frames directly (that should change as the head unit is designed to have the UIs not reading/writing directly to the CAN networks

## TODO

* Climate control UI
* Audio panels UI
* Radio/CD UI
* Telematics/KML/Phone UI
* Basic (turn by turn) navigation UI
* Full (map) navigation UI
* Complete trip computer UI
* TPMS UI
* Diagnostics interface (ideally be detected as a real EMF by diagbox)
* Configuration to toggle the UIs
