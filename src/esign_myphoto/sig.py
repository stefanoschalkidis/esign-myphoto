import logging as log
from dataclasses import dataclass

import win32com.client

from esign_myphoto import i18n
from esign_myphoto.config import SigConfig


@dataclass
class CaptureResult:
    data: str | None
    msg: str


def capture_signature(
    sig_config: SigConfig, last_name: str, first_name: str
) -> CaptureResult:
    data: str | None = None

    sig_ctl = win32com.client.Dispatch("Florentis.SigCtl.1")
    sig_key = win32com.client.Dispatch("Florentis.Key.1")
    sig_hash = win32com.client.Dispatch("Florentis.Hash.1")
    dyn_cap = win32com.client.Dispatch("Florentis.DynamicCapture.1")

    sig_ctl.Licence = sig_config.license
    sig_key.Set(7)
    sig_hash.Type = 6
    sig_hash.Add(sig_config.reason)
    dyn_cap.SetProperty("UILanguage", i18n.tr.LANG_CODE)
    log.info(i18n.tr.MSG_CAPTURING_SIGNATURE)

    dyn_cap_result = dyn_cap.Capture(
        sig_ctl,
        f"{last_name} {first_name}",
        sig_config.reason,
        sig_hash,
        sig_key,
    )

    match dyn_cap_result:
        case 0:
            data = sig_ctl.Signature.RenderBitmap(
                "not_provided",
                sig_config.image_width,
                sig_config.image_height,
                sig_config.mime_type,
                sig_config.ink_width,
                sig_config.ink_color,
                sig_config.background_color,
                sig_config.padding_x,
                sig_config.padding_y,
                sig_config.flags,
            )
            msg = i18n.tr.MSG_CAPTURE_SUCCESSFUL
        case 1:
            msg = i18n.tr.MSG_SIG_CAPTURE_CANCELLED
        case 100:
            msg = i18n.tr.ERR_NO_DIGITIZER_CONNECTED
        case 103:
            msg = i18n.tr.ERR_WACOM_SDK_NOT_LICENSED
        case _:
            msg = f"Wacom error number {dyn_cap_result}."

    return CaptureResult(data, msg)
