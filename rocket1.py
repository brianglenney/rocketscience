from ggrocket import Rocket, Planet

moon = Planet(viewscale=0.00005, planetmass=7.348E22, radius=1737000)
rocket = Rocket(moon, altitude=1837000, velocity=1000, timezoom=3)
moon.run(rocket)
