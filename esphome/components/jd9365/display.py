from esphome import pins, core
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display
from esphome.components.esp32 import const, only_on_variant

from esphome.const import (
    CONF_ID,
    CONF_RESET_PIN,
)

DEPENDECIES = ["esp_ldo"]

_ns = cg.esphome_ns.namespace("jd9365")
_cls = _ns.class_("JD9365", display.Display, cg.Component)

CONFIG_SCHEMA = cv.All(
    display.FULL_DISPLAY_SCHEMA.extend(
        cv.Schema({
            cv.GenerateID(): cv.declare_id(_cls),
            cv.Required(CONF_RESET_PIN): pins.internal_gpio_input_pin_schema,
        })
    ),
    cv.only_with_esp_idf,
)

async def to_code(config):
    # add_idf_sdkconfig_option("CONFIG_LOG_DEFAULT_LEVEL_DEBUG", "y")
    # add_idf_component(
    #     name="esp_lcd_jd9365",
    #     repo="https://github.com/espressif/esp-iot-solution.git",
    #     ref="master",
    #     path="components/display/lcd/esp_lcd_jd9365",
    #     refresh=core.TimePeriodMinutes(60),
    # )
    var = cg.new_Pvariable(config[CONF_ID])
    await display.register_display(var, config)
    cg.add(var.set_reset_pin(await cg.gpio_pin_expression(config.get(CONF_RESET_PIN))))
