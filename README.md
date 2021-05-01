# Home Assistant Kasa HS100 Control
A custom integration for home assistant to control the Kasa HS100 plugs. 99.9% of the credit goes to these lovely people below. I just hacked my way through it all to get it working for the HS100!

I've tested with an HS100 for about a week and all working great. I am a novice coder (understatement!), so I can't offer a huge ammount of support or gurantee it won't melt your HA server.

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

## Contributing
Pull requests are welcome.

## Upcoming Features:
* Support for HS100
* Assumed support for HS110 (not tested)

## Contributors
* [python-kasa](https://github.com/python-kasa/python-kasa)
* [ghostseven](https://github.com/ghostseven/python-kasa)
* [fishbigger](https://github.com/fishbigger/HomeAssistant-Tapo-P100-Control)


## License
[MIT](https://choosealicense.com/licenses/mit/)
