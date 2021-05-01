# Home Assistant Kasa HS100 Control
A custom integration for home assistant to control Kasa HS100 plugs. This works with the latest 1.1.0 firmware which disables support for HA (and other 3rd party products) in the UK versions of the plug.

I've tested with an HS100 for about a week and all working great. I am a novice coder (understatement!), so I can't offer a huge ammount of support or gurantee it won't melt your HA.

99.9% of the credit goes to the lovely people below. I just hacked my way through it all to get it working for the HS100.

## Installation

To install the Kasa HS100 integration copy the `kasa_hs100_control` folder into the `custom_components` folder on your home assistant instance then these lines should be added to your `configuration.yaml` file. 

```yaml

#HS100 or (I thinkk) HS110 Plug
switch:
    platform: kasa_hs100_control
    host: 192.168.x.x
    username: email@gmail.com
    password: Password123
    
```
Note: Plug must be added to your TP-Link accoount in the Kasa app. I could not get a local only plug to work. You can disable the internet for you polug in your router to block it updating in future.

## Contributing
Pull requests are welcome.

## Supported Devices:
* Support for HS100
* Assumed support for HS110 (not tested)

## Contributors
* [python-kasa](https://github.com/python-kasa/python-kasa) for the awessome code to connect to Kasa devices.
* [ghostseven](https://github.com/ghostseven/python-kasa) for the fix to connect to the new Kasa protocol. This is the version being used.
* [fishbigger](https://github.com/fishbigger/HomeAssistant-Tapo-P100-Control) for the Tapo custom component which I adapted for this.


## License
[MIT](https://choosealicense.com/licenses/mit/)
