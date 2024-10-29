from abc import ABC, abstractmethod
import time

class Transportasi(ABC):
    """Interface Transportasi"""
    def __init__(self, bahan_bakar, kecepatan):
        self.bahan_bakar = bahan_bakar
        self.kecepatan = kecepatan

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def status(self):
        pass

class Roda:
    """Class Roda"""
    def __init__(self, jenis_roda):
        self.jenis_roda = jenis_roda
        print(f"Roda jenis '{self.jenis_roda}' dibuat.")

class Mesin:
    """Class Mesin"""
    def __init__(self, tenaga):
        self.tenaga = tenaga
        self.status_mesin = False
        print(f"Mesin dengan tenaga {self.tenaga} HP dibuat.")

    def nyalakan_mesin(self):
        self.status_mesin = True
        print("Mesin dinyalakan.")

    def matikan_mesin(self):
        self.status_mesin = False
        print("Mesin dimatikan.")

class Setir:
    """Class Setir"""
    def __init__(self, tipe_setir):
        self.tipe_setir = tipe_setir
        print(f"Setir tipe '{self.tipe_setir}' dibuat.")


class Fuel(Transportasi):
    """Class Fuel (turunan dari Transportasi)"""
    def __init__(self, bahan_bakar, kecepatan):
        super().__init__(bahan_bakar, kecepatan)

    def start(self):
        print("Fuel start")

    def drive(self):
        print("Fuel drive")

    def status(self):
        print(f"Fuel - Bahan Bakar: {self.bahan_bakar}, Kecepatan: {self.kecepatan} km/h")

# Class AutoCar (turunan dari Transportasi)
class AutoCar(Transportasi):
    def __init__(self, bahan_bakar, kecepatan, tenaga_mesin):
        super().__init__(bahan_bakar, kecepatan)
        self.roda = [Roda("All-Terrain") for _ in range(4)]  # Komposisi dengan 4 roda
        self.mesin = Mesin(tenaga_mesin)  # Komposisi dengan satu mesin
        self.setir = Setir("Power Steering")  # Komposisi dengan satu setir
        self.sedang_berjalan = False
        print("AutoCar dibuat")

    def start(self):
        if not self.mesin.status_mesin:
            self.mesin.nyalakan_mesin()
            print("AutoCar siap digunakan.")
        else:
            print("AutoCar sudah menyala.")

    def drive(self, durasi=5):
        if self.mesin.status_mesin:
            if self.bahan_bakar > 0:
                self.sedang_berjalan = True
                print("AutoCar mulai berjalan...")
                for i in range(durasi):
                    if self.bahan_bakar <= 0:
                        print("Bahan bakar habis! AutoCar berhenti.")
                        self.sedang_berjalan = False
                        break
                    self.bahan_bakar -= 1
                    print(f"Kecepatan: {self.kecepatan} km/h, Bahan Bakar Tersisa: {self.bahan_bakar} L")
                    time.sleep(1)
                print("AutoCar berhenti.")
            else:
                print("Tidak ada cukup bahan bakar untuk berjalan.")
        else:
            print("Nyalakan mesin terlebih dahulu!")

    def status(self):
        mesin_status = "Menyala" if self.mesin.status_mesin else "Mati"
        print(f"Status AutoCar -> Mesin: {mesin_status}, Bahan Bakar: {self.bahan_bakar} L, Kecepatan: {self.kecepatan} km/h")


class Mio(Transportasi):
    """Class Mio (turunan dari Transportasi)"""
    def __init__(self, bahan_bakar, kecepatan):
        super().__init__(bahan_bakar, kecepatan)

    def start(self):
        print("Mio started")

    def drive(self):
        print("Mio driving")

    def status(self):
        print(f"Mio - Bahan Bakar: {self.bahan_bakar}, Kecepatan: {self.kecepatan} km/h")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat instance dari AutoCar
    auto_car = AutoCar(bahan_bakar=10, kecepatan=80, tenaga_mesin=150)
    auto_car.status()  # Menunjukkan status awal
    auto_car.start()   # Menyalakan mesin
    auto_car.drive(durasi=10)  # Mengemudi selama 10 detik
    auto_car.status()  # Menunjukkan status setelah berkendara

    print("\n")

    # Membuat instance Mio
    mio = Mio(bahan_bakar=5, kecepatan=60)
    mio.start()
    mio.status()
