# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from openfisca_france.model.prelevements_obligatoires.prelevements_sociaux.cotisations_sociales.allegements import *
from openfisca_core.periods import *
from openfisca_france import FranceTaxBenefitSystem

def test_coefficient_proratisation_only_contract_periods():
  tax_benefit_system = FranceTaxBenefitSystem()
  scenario = tax_benefit_system.new_scenario()
  scenario.init_single_entity(period='2017-11',
    parent1=dict(salaire_de_base=2300,
    effectif_entreprise=1,
    code_postal_entreprise="75001",
    categorie_salarie=u'prive_non_cadre',
    contrat_de_travail_debut='2017-11-1',
    allegement_fillon_mode_recouvrement=u'progressif'))
  simulation = scenario.new_simulation()
  assert_equal(simulation.calculate_add('coefficient_proratisation','2017-11'),1)
  assert_equal(simulation.calculate_add('coefficient_proratisation','2017-12'),1)
  assert_equal(simulation.calculate_add('coefficient_proratisation','2017-10'),0)
  assert_equal(simulation.calculate_add('coefficient_proratisation','2017'),2)
