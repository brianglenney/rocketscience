from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.00005)
rocket = Rocket(earth, altitude=4000000, velocity=6199.39875, timezoom=2)
earth.run(rocket)
