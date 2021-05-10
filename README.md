# Cowin_Alert
For Alerting available slots on Cowin portal (Covid Vaccination)

- Requires beepy (pip install beeply)
- Works only in windows
- Checks every 30 seconds and makes a beep sound if any slot is available in your district.
- You will have to go and book the appointment manually, this is only for alerting you.

You can get your district_id from the URLS APIs Below
 
- State_ID = https://cdn-api.co-vin.in/api/v2/admin/location/states
- District_ID = https://cdn-api.co-vin.in/api/v2/admin/location/districts/{State_ID}
