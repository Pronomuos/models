from Brownian_motion import BrownianMotion

if __name__ == '__main__':
    # Вода
    """
    water = BrownianMotion(temp=100, nu=282.5e-6, r=1.38e-9, time=60, intervals=100, m=3e-26)
    print("Коэффициент диффузии = ", water.find_diffusion(), " м^2/с.")
    print("Средняя длина свободного пробега = ", water.find_free_path(), " см.")
    boltzmann = 0
    for i in range(0, 5):
        water.plot_trajectory()
        boltzmann += water.calc_boltzmann()
    print("Постоянная Больцмана = ", boltzmann / 5)
    """

    # Азот
    """
    nitrogen = BrownianMotion(temp=400, nu=26e-6, r=1.5e-10, time=60, intervals=200, m=28.3e-26)
    print("Коэффициент диффузии = ", nitrogen.find_diffusion(), " м^2/с.")
    print("Средняя длина свободного пробега = ", nitrogen.find_free_path(), " см.")
    boltzmann = 0
    for i in range(0, 5):
        nitrogen.plot_trajectory()
        boltzmann += nitrogen.calc_boltzmann()
    print("Постоянная Больцмана = ", boltzmann / 5)
    """

    # Водород
    hydrogen = BrownianMotion(temp=375, nu=1.04e-5, r=1.25e-10, time=60, intervals=150, m=3.3e-27)
    print("Коэффициент диффузии = ", hydrogen.find_diffusion(), " м^2/с.")
    print("Средняя длина свободного пробега = ", hydrogen.find_free_path(), " см.")
    boltzmann = 0
    for i in range(0, 5):
        hydrogen.plot_trajectory()
        boltzmann += hydrogen.calc_boltzmann()
    print("Постоянная Больцмана = ", boltzmann / 5)

