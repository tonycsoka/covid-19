from parameters_cov import params
from math import exp, ceil, log, floor, sqrt
import numpy as np
from scipy.integrate import ode
from scipy.stats import norm, gamma
import pandas as pd
##
# -----------------------------------------------------------------------------------
##
class simulator:
    def __init__(self):
        pass
    ##
#-----------------------------------------------------------------
        
    ##
    def poly_solv_ode(self,t,y,beta_L_factor=1,beta_H_factor=1,t_control=None,vaccine_time=None,ICU_grow=0):
        ##
        S_L = y[params.S_L_ind]
        I_L = y[params.I_L_ind]
        H_L = y[params.H_L_ind]
        C_L = y[params.C_L_ind]

        vaccine_effect_H = 0
        vaccine_effect_L = 0
        if vaccine_time is not None:
            if t>365*(vaccine_time/12):
                if y[params.S_H_ind]> (1-params.vaccinate_percent)*params.hr_frac: # vaccinate 90%
                    vaccine_effect_H = params.vaccinate_rate
                elif y[params.S_L_ind]> (1-params.vaccinate_percent)*(1-params.hr_frac):  # vaccinate 90%
                    vaccine_effect_L = params.vaccinate_rate


        S_H = y[params.S_H_ind]
        I_H = y[params.I_H_ind]
        H_H = y[params.H_H_ind]
        C_H = y[params.C_H_ind]




        
        if t_control is None:
            beta_L_factor = 1
            beta_H_factor = 1
        else:
            if len(t_control)>1:
                if t<t_control[0] or t>t_control[1]:
                    beta_L_factor = 1
                    beta_H_factor = 1

        ICU_capac = params.ICU_capacity*(1 + ICU_grow*t/365 )
        if C_L>ICU_capac:
            C_L_to_R_L = ICU_capac*params.crit_recovery
            C_L_to_D_L = ICU_capac*params.crit_death + params.noICU*(params.crit_death + params.crit_recovery)*(C_L-ICU_capac) # all without crit care die
        else:
            C_L_to_R_L = C_L*params.crit_recovery
            C_L_to_D_L = C_L*params.crit_death

        if C_H>ICU_capac:
            C_H_to_R_H = ICU_capac*params.crit_recovery
            C_H_to_D_H = ICU_capac*params.crit_death + params.noICU*(params.crit_death + params.crit_recovery)*(C_H-ICU_capac) # all without crit care die
        else:
            C_H_to_R_H = C_H*params.crit_recovery
            C_H_to_D_H = C_H*params.crit_death
        
        dydt = [-S_L*( params.beta*(beta_L_factor**2)*I_L  +  (params.beta*((beta_H_factor*beta_L_factor)**1))*I_H ) - vaccine_effect_L, # dS
                +S_L*( params.beta*(beta_L_factor**2)*I_L  +  (params.beta*((beta_H_factor*beta_L_factor)**1))*I_H ) - params.mu_L*I_L - params.gamma_L*I_L + (1-params.hr_frac)*params.import_rate, # dI
                I_L*params.mu_L    + H_L*params.recover_L + C_L_to_R_L + vaccine_effect_L  - (1-params.hr_frac)*params.import_rate,  # dR
                I_L*params.gamma_L - H_L*params.recover_L - H_L*params.crit_L,         # dH
                H_L*params.crit_L  - (C_L_to_R_L + C_L_to_D_L),                          # dC
                + C_L_to_D_L,                                                      # dD
                -S_H*( (params.beta*((beta_H_factor*beta_L_factor)**1))*I_L + params.beta*(beta_H_factor**2)*I_H) - vaccine_effect_H , # dS
                +S_H*( (params.beta*((beta_H_factor*beta_L_factor)**1))*I_L + params.beta*(beta_H_factor**2)*I_H) - params.mu_H*I_H - params.gamma_H*I_H + params.hr_frac*params.import_rate, # dI
                I_H*params.mu_H    + H_H*params.recover_H  + C_H_to_R_H + vaccine_effect_H -  params.hr_frac*params.import_rate,           # dR
                I_H*params.gamma_H - H_H*params.recover_H - H_H*params.crit_H,         # dH
                H_H*params.crit_H  - (C_H_to_R_H + C_H_to_D_H),                          # dC
                + C_H_to_D_H                                                       # dD
                ]
        
        return dydt
    ##
    #--------------------------------------------------------------------
    ##
    def poly_calc_ode(self,I0,R0,H0,C0,D0,beta_L_factor,beta_H_factor,t_control,T_stop,vaccine_time,ICU_grow): # critical,death
        
        I0_L = (1-params.hr_frac)*params.N*I0
        R0_L = (1-params.hr_frac)*params.N*R0
        C0_L = (1-params.hr_frac)*params.N*C0
        H0_L = (1-params.hr_frac)*params.N*H0
        D0_L = (1-params.hr_frac)*params.N*D0
        S0_L = (1-params.hr_frac)*params.N - I0_L - R0_L - C0_L - H0_L - D0_L
        
        I0_H = params.hr_frac*params.N*I0
        R0_H = params.hr_frac*params.N*R0
        C0_H = params.hr_frac*params.N*C0
        H0_H = params.hr_frac*params.N*H0
        D0_H = params.hr_frac*params.N*D0
        S0_H = params.hr_frac*params.N - I0_H - R0_H - C0_H - H0_H - D0_H

        
        
        y0 = [S0_L,
            I0_L,
            R0_L,
            C0_L,
            H0_L,
            D0_L,
            S0_H,
            I0_H,
            R0_H,
            C0_H,
            H0_H,
            D0_H,
            ]
        # print(y0)

        sol = ode(self.poly_solv_ode,jac=None).set_integrator('dopri5').set_f_params(beta_L_factor,beta_H_factor,t_control,vaccine_time,ICU_grow) # ,critical,death
        
        tim = np.linspace(0,T_stop, 301) # use 141 time values

        
        sol.set_initial_value(y0,tim[0])

        y_out = np.zeros((len(y0),len(tim)))
        
        i2 = 0
        y_out[:,0] = sol.y
        for t in tim[1:]:
                if sol.successful():
                    sol.integrate(t)
                    i2=i2+1
                    y_out[:,i2] = sol.y
                else:
                    raise RuntimeError('ode solver unsuccessful')
        
        return y_out, tim

    ##
    #--------------------------------------------------------------------
    ##
    def run_model(self,beta_L_factor=1,beta_H_factor=1,t_control=None,T_stop=params.T_stop,vaccine_time=None,I0=params.initial_infections,R0=0,H0=0,C0=0,D0=0,ICU_grow=0):
        # print(I0_H*60*10**6,I0_L*60*10**6,params.hr_frac)
        y_out, tim = self.poly_calc_ode(I0=I0,R0=R0,H0=H0,C0=C0,D0=D0,beta_L_factor=beta_L_factor,beta_H_factor=beta_H_factor,t_control=t_control,T_stop=T_stop,vaccine_time=vaccine_time,ICU_grow=ICU_grow) # critical=critical,death=death,
        dicto = {'y': y_out,'t': tim,'beta_L': beta_L_factor,'beta_H': beta_H_factor}
        return dicto
#--------------------------------------------------------------------


