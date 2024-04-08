from homeassistant.const import CONF_ENTITY_ID
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

DOMAIN = "cover"
CONF_SPEED = 'speed'
CONF_POSITION = 'position'
SET_COVER_POSITION_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ENTITY_ID): cv.entity_ids,
        vol.Required(CONF_POSITION): vol.Range(min=0, max=100),
        vol.Optional(CONF_SPEED, default=255): vol.Range(min=1, max=255),
    },
)
