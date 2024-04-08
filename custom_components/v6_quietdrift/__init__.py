"""QuietDrift support for SwitchBot Curtain devices by v6ak"""

from homeassistant import core
import logging
from typing import Any
from homeassistant.core import HomeAssistant
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import entity_registry
from homeassistant.const import CONF_ENTITY_ID

from .const import CONF_SPEED, CONF_POSITION, DOMAIN, SET_COVER_POSITION_SCHEMA

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:

    async def handle_set_cover_position(service_call: ServiceCall):
        data = service_call.data
        
        speed = data[CONF_SPEED]
        position = data[CONF_POSITION]
        
        entity_ids = data[CONF_ENTITY_ID]
        ent_reg = entity_registry.async_get(hass)
        registry_entities = list(map(ent_reg.async_get, entity_ids))
        entities = list(map(lambda re: hass.data['cover'].get_entity(re.entity_id), registry_entities))
        
        for entity in entities:
          res = await entity._device.set_position(position=position, speed=speed)
          (_LOGGER.info if res else _LOGGER.warn)('set position (%s, %d, %d) result: %s', entity.entity_id, position, speed, res)

    hass.services.async_register(
        domain=DOMAIN,
        service='v6_set_switchbot_curtain_position',
        service_func=handle_set_cover_position,
        schema=SET_COVER_POSITION_SCHEMA,
    )

    return True
