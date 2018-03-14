from ggrocket import Rocket, Planet

moon = Planet(viewscale=0.00005)
rocket = Rocket(earth, altitude=1179600, velocity=2000, timezoom=2)
earth.run(rocket)
