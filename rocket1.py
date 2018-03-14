from ggrocket import Rocket, Planet

moon = Planet(viewscale=0.00005, planetmass=7.348E22, radius=1079600)
rocket = Rocket(earth, altitude=1179600, velocity=2000, timezoom=2)
moon.run(rocket)
