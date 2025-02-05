import numpy as np
from src.funcs.base import ABECEDARY, lil_endian, setup_logger
from src.funcs.format import fmt_biparticion
from src.middlewares.observer import DebugObserver
from controllers.manager import Manager
from src.models.base.sia import SIA

import math

import pyphi
from pyphi.labels import NodeLabels
from pyphi import Network, Subsystem
from pyphi.models.cuts import Bipartition, Part

from src.middlewares.profile import profile, profiler_manager
from src.models.core.solution import Solution

from models.base.application import aplicacion

from src.models.enums.distance import MetricDistance
from src.constants.base import (
    STR_ONE,
)


class Phi(SIA):
    """Class Phi is used as base for other strategies, bruteforce with pyphi."""

    def __init__(self, config: Manager) -> None:
        super().__init__(config)
        profiler_manager.start_session(
            f"NET{len(config.estado_inicial)}{config.pagina}"
        )
        self.logger = setup_logger("bruteforce_analysis")
        self.debug_observer = DebugObserver()

    @profile(context={"type": "pyphi_analysis"})
    def aplicar_estrategia(self, condiciones: str, alcance: str, mecanismo: str):
        pyphi.config.WELCOME_OFF = "yes"
        estado_inicial = tuple(int(s) for s in self.sia_loader.estado_inicial)
        tamanho = len(estado_inicial)

        indices = tuple(range(tamanho))
        etiquetas = tuple(ABECEDARY[:tamanho])

        completo = NodeLabels(etiquetas, indices)
        mpt_estados_nodos_on = self.sia_cargar_tpm()
        red = Network(tpm=mpt_estados_nodos_on, node_labels=completo)

        candidato = tuple(
            completo[i] for i, bit in enumerate(condiciones) if bit == STR_ONE
        )
        subsistema = Subsystem(network=red, state=estado_inicial, nodes=candidato)
        alcance = tuple(
            ind
            for ind, (bit, cond) in enumerate(zip(alcance, condiciones))
            if (bit == STR_ONE) and (cond == STR_ONE)
        )
        mecanismo = tuple(
            ind
            for ind, (bit, cond) in enumerate(zip(mecanismo, condiciones))
            if (bit == STR_ONE) and (cond == STR_ONE)
        )

        mip = (
            subsistema.effect_mip(mecanismo, alcance)
            if aplicacion.distancia_metrica == MetricDistance.EMD_EFECTO.value
            else subsistema.cause_mip(mecanismo, alcance)
        )
        small_phi: float = mip.phi

        repertorio = mip.repertoire.flatten()
        repertorio_partido = mip.partitioned_repertoire.flatten()

        states = int(math.log2(mip.repertoire.size))
        sub_states: np.ndarray = lil_endian(states)

        repertorio.put(sub_states, repertorio)
        repertorio_partido.put(sub_states, repertorio_partido)

        mejor_biparticion: Bipartition = mip.partition
        prim: Part = mejor_biparticion.parts[True]
        dual: Part = mejor_biparticion.parts[False]

        prim_mech, prim_purv = prim.mechanism, prim.purview
        dual_mech, dual_purv = dual.mechanism, dual.purview
        format = fmt_biparticion(
            [dual_purv, dual_mech],
            [prim_purv, prim_mech],
        )

        return Solution(
            estrategia="Pyphi",
            perdida=small_phi,
            distribucion_subsistema=repertorio,
            distribucion_particion=repertorio_partido,
            particion=format,
        )
