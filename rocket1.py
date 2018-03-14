from ggrocket import Rocket, Planet

moon = Planet(viewscale=0.00005, planetmass=7.348E22, radius=1079600)
rocket = Rocket(moon, altitude=1179600, velocity=1475, timezoom=3)
moon.run(rocket)
