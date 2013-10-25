from math import sqrt

class particle():
    def __init__(self):
        self.spin = 0.0
        self.mass = 0.0 #in GeV, natural units
        self.charge = 0.0 #Charge is multiplied by 3, so don't have to deal with fractions
        self.pdg_id = 0
        self.momentum = 0.0
        self.energy = 0.0

    def set_charge(self,new_charge):
        self.charge=new_charge

    def set_mass(self,new_mass):
        self.mass=new_mass

    def set_spin(self,new_spin):
        self.spin=new_spin

    def set_pdg_id(self,new_id):
        self.pdg_id=new_id

    def set_momentum(self,new_mom):
        self.momentum = new_mom

    def set_energy(self,new_energy):
        self.energy = new_energy

    def get_charge(self):
        return self.charge

    def get_mass(self):
        return self.mass

    def get_spin(self):
        return self.spin

    def get_pdg_id(self):
        return self.pdg_id

    def get_momentum(self):
        return self.momentum

    def get_energy(self):
        return self.energy

    def __str__(self):
        return "You created a {} with energy {}.".format(self.__class__.__name__,str(self.energy))

class boson(particle):
    def __init__(self):
        particle.__init__(self)
        self.set_spin(1)

class lepton(particle):
    def __init__(self):
        particle.__init__(self)
        self.lepton_num=1
        self.set_spin(0.5)

    def set_lepton_num(self,new_num):
        self.lepton_num=new_num

    def get_lepton_num(self):
        return self.lepton_num

class quark(particle):
    def __init__(self):
        particle.__init__(self)
        self.baryon_num = 1
        self.isospin = 0.5
        self.colour=1
        self.colour_dict = {'r':1, 'b':2, 'g':3}
        self.set_spin(0.5)

    def set_colour(self,new_colour):
        self.colour=self.colour_dict[new_colour]

    def set_isospin(self,new_iso):
        self.isospin=new_iso

    def set_baryon_num(self,new_num):
        self.baryon_num=new_num

    def get_colour(self):
        return self.colour

    def get_isospin(self):
        return self.isospin

    def get_baryon_num(self):
        return self.baryon_num

    def combine(self,quark2,quark3=None):
        if quark3!=None:
            print "hadron created!"
        else:
            print "meson created!"

class gluon(boson):
    def __init__(self,energy):
        boson.__init__(self)
        self.set_pdg_id(21)
        self.set_energy(energy)
        self.set_momentum(energy)

class photon(boson):
    def __init__(self, energy):
        boson.__init__(self)
        self.set_pdg_id(22)
        self.set_energy(energy)
        self.set_momentum(energy) #Photon energy equals momentum, at high E, in natural units

class wplus(boson):
    def __init__(self,energy):
        boson.__init__(self)
        self.set_pdg_id(24)
        self.set_charge(3)
        self.set_mass(80.39)
        self.set_energy(energy)
        self.set_momentum(sqrt(self.energy^2 + self.mass^2))

class wminus(boson):
    def __init__(self,energy):
        boson.__init__(self)
        self.set_pdg_id(-24)
        self.set_charge(-3)
        self.set_mass(80.39)
        self.set_energy(energy)
        self.set_momentum(sqrt(self.energy^2 + self.mass^2))

class z_boson(boson):
    def __init__(self,energy):
        boson.__init__(self)
        self.set_pdg_id(23)
        self.set_mass(91.19)
        self.set_energy(energy)
        self.set_momentum(sqrt(self.energy^2 + self.mass^2))

class up_q(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(2)
        self.set_energy(energy)
        self.set_momentum(energy) #p^2 = E^2 - m^2 ~ E^2 at high E, given low mass of up quark
        self.set_pdg_id(2)

class u_bar(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(-2)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-2)
        self.set_baryon_num(-1)

class down_q(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(-1)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(1)

class d_bar(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(1)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-1)
        self.set_baryon_num(-1)

class strange_q(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(-1)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(3)
        self.strangeness=1

    def get_strangeness(self):
        return self.strangeness

class s_bar(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(1)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-3)
        self.strangeness=-1

    def get_strangeness(self):
        return self.strangeness

class charm_q(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(2)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(4)

class c_bar(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(-2)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-4)

class bottom_q(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(-1)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(5)

class b_bar(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(1)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-5)

class top_q(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(2)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(6)

class t_bar(quark):
    def __init__(self,energy):
        quark.__init__(self)
        self.set_charge(-2)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-6)

class electron(lepton):
    def __init__(self,energy):
        lepton.__init__(self)
        self.set_charge(-3)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(11)

class positron(lepton):
    def __init__(self,energy):
        lepton.__init__(self)
        self.set_charge(3)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-11)
        self.set_lepton_num(-1)

class muon(lepton):
    def __init__(self,energy):
        lepton.__init__(self)
        self.set_charge(-3)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(13)

class antimuon(lepton):
    def __init__(self,energy):
        lepton.__init__(self)
        self.set_charge(3)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-13)

class tau(lepton):
    def __init__(self,energy):
        lepton.__init__(self)
        self.set_charge(-3)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(15)

class antitau(lepton):
    def __init__(self,energy):
        lepton.__init__(self)
        self.set_charge(3)
        self.set_energy(energy)
        self.set_momentum(energy)
        self.set_pdg_id(-15)


