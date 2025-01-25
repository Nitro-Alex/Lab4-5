class Service:
    def __init__(self, name="Новый тариф", cost=0.0):
        self.name = name
        self.cost = cost

    def __del__(self):
        print("Тариф удалён")

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_cost(self, new_cost):
        self.cost = new_cost

    def get_cost(self):
        return self.cost


class Resident:
    def __init__(self, surname="-", name="-"):
        self.name = name
        self.surname = surname
        self.consumption = []

    def __del__(self):
        print("Жилец удалён")

    def set_name(self, new_surname, new_name):
        self.name = new_name
        self.surname = new_surname

    def get_surname(self):
        return self.surname

    def get_name(self):
        return self.name

    def use_service(self, service):
        self.consumption.append(service)

    def summ_service(self):
        return sum(service.get_cost() for service in self.consumption)

    def clear_consumption(self):
        self.consumption.clear()

class Ges:
    def __init__(self, district="-", number=0):
        self.district = district
        self.number = number
        self.residents = []
        self.services = []

    def __del__(self):
        print("ЖЭС удалена")

    def set_district(self, new_district):
        self.district = new_district

    def set_number(self, new_number):
        self.number = new_number

    def get_services(self):
        return self.services

    def get_residents(self):
        return self.residents

    def add_service(self, service):
        self.services.append(service)

    def add_resident(self, resident):
        self.residents.append(resident)

    def find_res(self, surname):
        for resident in self.residents:
            if resident.get_surname() == surname:
                return resident

    def find_service(self, service_name):
        for service in self.services:
            if service.get_name() == service_name:
                return service

    def clear_services(self):
        self.services.clear()

    def clear_residents(self):
        self.residents.clear()

    def clear_notes(self):
        for resident in self.residents:
            resident.clear_consumption()

    def total_cost(self):
        return sum(resident.summ_service() for resident in self.residents)

    def get_data(self):
        data = []
        for resident in self.residents:
            data.append((resident.get_surname(), resident.get_name(), resident.summ_service()))
        return data