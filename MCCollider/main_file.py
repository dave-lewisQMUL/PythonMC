__author__ = 'Dave'

from random import randint
from particles import *

def get_rndm(min_,max_):
    return randint(min_,max_)

if __name__=="__main__":
    print """

    ====================
    Welcome to PythonMC!
    ====================

    """

    energy = float(raw_input("Initial energy in GeV: "))
    initial_e=electron(energy)
    initial_p=positron(energy)
    initial_p.set_momentum(-energy)
    seed=get_rndm(1,100)
    if seed<30:
        final_p1=up_q(energy)
        final_p2=u_bar(energy)
    elif seed<70:
        final_p1=electron(energy)
        final_p2=positron(energy)
    elif seed<80:
        final_p1=down_q(energy)
        final_p2=d_bar(energy)
    elif seed<90:
        final_p1=muon(energy)
        final_p2=antimuon(energy)
    elif seed<98:
        final_p1=electron(2*energy/3)
        final_p2=positron(2*energy/3)
        final_p3=photon(2*energy/3)
    elif seed<=100:
        final_p1=bottom_q(energy)
        final_p2=b_bar(energy)

    try:
        print """
    ------------
    You created a {}, {} and {} with
    energies {}, {}, {} respectively.
    ------------""".format(final_p1.__class__.__name__,
                            final_p2.__class__.__name__,
                            final_p3.__class__.__name__,
                            final_p1.get_energy(),
                            final_p2.get_energy(),
                            final_p3.get_energy())

    except NameError:

        print """
    ------------
    You created a {} and {} with
    energies {} and {} respectively.
    ------------""".format(final_p1.__class__.__name__,
                            final_p2.__class__.__name__,
                            final_p1.get_energy(),
                            final_p2.get_energy())
    except:
        print "oops, something went wrong!"
        raise