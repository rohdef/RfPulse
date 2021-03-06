# RfPulseLib
#
# Copyright (C) 2011 by Rohde Fischer <rohdef@rohdef.dk> www.rohdef.dk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import ctypes
from ctypes import *

import lib
#_pa = lib.LibraryLoader().load_library('pulse')
_pa = lib.load_library('pulse')

#
# Helper functions
#

def getPa():
    '''Returns the PulseAudio library object that contains all the PulseAudio functions.
    
    Example of usage:
    pa = getPa()
    mainLoop = pa.pa_threaded_mainloop_new()
    mainLoopApi = pa.pa_threaded_mainloop_get_api(mainLoop)'''
    return _pa

#
# Classes and enum simulations
#

class ContextState():
    '''Enum simulation of the context states.
    
    Context states:
    UNCONNECTED
    CONNECTING
    AUTHORIZING
    SETTING_NAME
    READY
    FAILED
    TERMINATED
    
    Example of usage:
    def _contextStateCallback(self, context, userData):
        state = self._pa.pa_context_get_state(context)
        print 'Context state: {0}'.format(ContextState.states[state])
        
        if state == ContextState.CONNECTING:
            print 'Connecting, please wait'
        elif state == ContextState.AUTHORIZING:
            print 'Authorizing - I hope you have the right credentials :p'
        elif state == ContextState.READY:
            print 'Ready, start doing your work man :)'
        elif state == ContextState.FAILED:
            raise Exception('Could not connect, sorry mate.')'''
    states = {0: 'unconnected', 1: 'connecting', 2: 'autorizing', 3: 'setting_name', 4: 'ready', 5: 'failed', 6: 'terminated'}
    
    UNCONNECTED = 0
    CONNECTING = 1
    AUTHORIZING = 2
    SETTING_NAME = 3
    READY = 4
    FAILED = 5
    TERMINATED = 6


#
# Data types and structs
#

pa_usec_t = c_uint64 # TODO inspect further
pa_sample_format_t = c_int # TODO create enum-like for this
pa_channel_position_t = c_int # TODO create enum-like for this
pa_volume_t = c_uint32 # TODO inspect this further

pa_sink_flags_t = c_int # enum
pa_sink_state_t = c_int # enum

pa_source_flags = c_int # enum
pa_source_state = c_int # enum


class pa_mainloop_struct(Structure):
    pass

class pa_threaded_mainloop_struct(Structure):
    pass

class pa_mainloop_api_struct(Structure):
    pass
    # TODO this really needs som work

class pa_operation_struct(Structure):
    pass

class pa_context_struct(Structure):
    pass

class pa_proplist_struct(Structure):
    pass # TODO This probably need work

class pa_sample_spec_struct(Structure):
    _fields_ = [("format", pa_sample_format_t),
        ("rate", c_uint32),
        ("channels", c_uint8)]

class pa_channel_map_struct(Structure):
    _fields_ = [("channels", c_uint8),
        ("map", pa_channel_position_t * 64)]

class pa_cvolume_struct(Structure):
    pass

pa_cvolume_struct._fields_ = [("channels", c_uint8),
        ("values", POINTER(pa_volume_t)) ]

class pa_sink_port_info_struct(Structure):
    _fields_ = [("name", c_char_p),
        ("description", c_char_p), ("priority", c_uint32)]

class pa_source_port_info_struct(Structure):
    _fields_ = [("name", c_char_p),
        ("description", c_char_p), ("priority", c_uint32)]

class pa_sink_info_struct(Structure):
    pass

pa_sink_info_struct._fields_ = [('name', c_char_p),
        ("index", c_uint32),
        ("description", c_char_p),
        ("sample_spec", pa_sample_spec_struct),
        ("channel_map", pa_channel_map_struct),
        ("owner_module", c_uint32),
        ("volume", pa_cvolume_struct),
        ("mute", c_int),
        ("monitor_source", c_uint32),
        ("monitor_source_name", c_char_p),
        ("latency", pa_usec_t),
        ("driver", c_char_p),
        ("flags", pa_sink_flags_t),
        ("proplist", pa_proplist_struct),
        ("configured_latency", pa_usec_t),
        ("base_volume", pa_volume_t),
        ("state", pa_sink_state_t),
        ("n_volume_steps", c_uint32),
        ("card", c_uint32),
        ("n_ports", c_uint32),
        ("ports", POINTER(pa_sink_port_info_struct)),
        ("active_port", POINTER(pa_sink_port_info_struct)),
        ("n_formats", c_uint8),
        ("formats", c_int)] # TODO wrong type!

class pa_source_info_struct(Structure):
    _fields_ = [("name", c_char_p),
        ("index", c_uint32),
        ("description", c_char_p),
        ("sample_spec", pa_sample_spec_struct),
        ("channel_map", pa_channel_map_struct),
        ("owner_module", c_uint32),
        ("volume", pa_cvolume_struct),
        ("mute", c_int),
        ("monitor_of_sink", c_uint32),
        ("monitor_of_sink_name", c_char_p),
        ("latency", pa_usec_t),
        ("driver", c_char_p),
        ("flags", pa_source_flags),
        ("proplist", pa_proplist_struct),
        ("configured_latency", pa_usec_t),
        ("base_volume", pa_volume_t),
        ("state", pa_source_state),
        ("n_volume_steps", c_uint32),
        ("card", c_uint32),
        ("n_ports", c_uint32),
        ("ports", pa_source_port_info_struct * 32),
        ("active_port", pa_source_port_info_struct)]

class pa_server_info_struct(Structure):
    _fields_ = [("user_name", c_char_p),
        ("host_name", c_char_p),
        ("server_version", c_char_p),
        ("server_name", c_char_p),
        ("sample_spec", pa_sample_spec_struct),
        ("default_sink_name", c_char_p),
        ("default_source_name", c_char_p),
        ("cookie", c_uint32),
        ("channel_map", pa_channel_map_struct)]

class pa_module_info_struct(Structure):
    _fields_ = [("index", c_uint32),
        ("name", c_char_p),
        ("argument", c_char_p),
        ("n_used", c_uint32),
        ("proplist", pa_proplist_struct)]

class pa_client_info_struct(Structure):
    _fields_ = [("index", c_uint32),
        ("name", c_char_p),
        ("owner_module", c_uint32),
        ("driver", c_char_p),
        ("proplist", pa_proplist_struct)]

class pa_card_profile_info_struct(Structure):
    _fields_ = [("name", c_char_p),
        ("description", c_char_p),
        ("n_sinks", c_uint32),
        ("n_sources", c_uint32),
        ("priority", c_uint32)]

class pa_card_info_struct(Structure):
    _fields_ = [("index", c_uint32),
        ("name", c_char_p),
        ("owner_module", c_uint32),
        ("driver", c_char_p),
        ("n_profiles", c_uint32),
        ("profiles", pa_card_profile_info_struct),
        ("active_profile", pa_card_profile_info_struct),
        ("proplist", pa_proplist_struct)]

class pa_sink_input_info_struct(Structure):
    pass
    
pa_sink_input_info_struct._fields_ = [("index", c_uint32),
        ("name", c_char_p),
        ("owner_module", c_uint32),
        ("client", c_uint32),
        ("sink", c_uint32),
        ("sample_spec", pa_sample_spec_struct),
        ("channel_map", pa_channel_map_struct),
        ("volume", pa_cvolume_struct),
        ("buffer_usec", pa_usec_t),
        ("sink_usec", pa_usec_t),
        ("resample_method", c_char_p),
        ("driver", c_char_p),
        ("mute", c_int),
        ("proplist", pa_proplist_struct)]

#
# Callback creation functions
#

contextNotifyCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(None))

# introspect.h
sinkInfoListCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_sink_info_struct), c_int, POINTER(None))
sourceInfoListCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_source_info_struct), c_int, POINTER(None))
serverInfoCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_server_info_struct), POINTER(None))
moduleInfoListCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_module_info_struct), c_int, POINTER(None))
clientInfoListCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_client_info_struct), c_int, POINTER(None))
cardInfoListCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_card_info_struct), c_int, POINTER(None))
sinkInputInfoListCallbackType = CFUNCTYPE(None, POINTER(pa_context_struct), POINTER(pa_sink_input_info_struct), c_int, POINTER(None))

#
# Function return types for the different header files
#
# This can be ignored by most developers
#

# context.h

_pa.pa_context_new.restype = POINTER(pa_context_struct)



# introspect.h

# Sinks
_pa.pa_context_get_sink_info_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_sink_info_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_sink_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_sink_volume_by_index.restype = POINTER(pa_operation_struct) # TODO
_pa.pa_context_set_sink_volume_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_sink_mute_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_sink_mute_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_suspend_sink_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_suspend_source_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_suspend_source_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_unload_module.restype = POINTER(pa_operation_struct)

# Sources
_pa.pa_context_get_source_info_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_source_info_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_source_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_source_volume_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_source_volume_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_source_mute_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_source_mute_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_suspend_source_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_suspend_source_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_source_port_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_source_port_by_name.restype = POINTER(pa_operation_struct)

# Server
_pa.pa_context_get_server_info.restype = POINTER(pa_operation_struct)

# Modules
_pa.pa_context_get_module_info.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_module_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_load_module.restype = POINTER(pa_operation_struct)
_pa.pa_context_unload_module.restype = POINTER(pa_operation_struct)

# Clients
_pa.pa_context_get_client_info.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_client_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_kill_client.restype = POINTER(pa_operation_struct)

# Cards
_pa.pa_context_get_card_info_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_card_info_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_card_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_card_profile_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_card_profile_by_name.restype = POINTER(pa_operation_struct)

# Sink inputs
_pa.pa_context_get_sink_input_info.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_sink_input_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_move_sink_input_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_move_sink_input_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_sink_input_volume.restype = POINTER(pa_operation_struct)
_pa.pa_context_set_sink_input_mute.restype = POINTER(pa_operation_struct)
_pa.pa_context_kill_sink_input.restype = POINTER(pa_operation_struct)

# Source outputs
_pa.pa_context_get_source_output_info.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_source_output_info_list.restype = POINTER(pa_operation_struct)
_pa.pa_context_move_source_output_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_move_source_output_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_kill_source_output.restype = POINTER(pa_operation_struct)

# Statistics
_pa.pa_context_stat.restype = POINTER(pa_operation_struct)

# Cached samples
_pa.pa_context_get_sample_info_by_name.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_sample_info_by_index.restype = POINTER(pa_operation_struct)
_pa.pa_context_get_sample_info_list.restype = POINTER(pa_operation_struct)


# mainloop.h
_pa.pa_mainloop_new.restype = POINTER(pa_mainloop_struct)
_pa.pa_mainloop_free.restype = None
_pa.pa_mainloop_get_api.restype = POINTER(pa_mainloop_api_struct)


# thread-mainloop.h
_pa.pa_threaded_mainloop_new.restype = POINTER(pa_threaded_mainloop_struct)
_pa.pa_threaded_mainloop_free.restype = None
_pa.pa_threaded_mainloop_stop.restype = None
_pa.pa_threaded_mainloop_lock.restype = None
_pa.pa_threaded_mainloop_unlock.restype = None
_pa.pa_threaded_mainloop_wait.restype = None
_pa.pa_threaded_mainloop_signal.restype = None
_pa.pa_threaded_mainloop_accept.restype = None
_pa.pa_threaded_mainloop_get_api.restype = POINTER(pa_mainloop_api_struct)


# volume.h
_pa.pa_cvolume_init.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_init.argtypes = [POINTER(pa_cvolume_struct)]

_pa.pa_cvolume_set.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_snprint.restype = c_char_p
_pa.pa_sw_cvolume_snprint_dB.restype = c_char_p
_pa.pa_volume_snprint.restype = c_char_p
_pa.pa_sw_volume_snprint_dB.restype = c_char_p
_pa.pa_cvolume_avg.restype = POINTER(pa_volume_t)
_pa.pa_cvolume_avg_mask.restype = POINTER(pa_volume_t)
_pa.pa_cvolume_max.restype = POINTER(pa_volume_t)
_pa.pa_cvolume_max_mask.restype = POINTER(pa_volume_t)
_pa.pa_cvolume_min.restype = POINTER(pa_volume_t)
_pa.pa_cvolume_min_mask.restype = POINTER(pa_volume_t)
_pa.pa_sw_volume_multiply.restype = POINTER(pa_volume_t)
_pa.pa_sw_cvolume_multiply.restype = POINTER(pa_cvolume_struct)
_pa.pa_sw_cvolume_multiply_scalar.restype = POINTER(pa_cvolume_struct)
_pa.pa_sw_volume_divide.restype = POINTER(pa_volume_t)
_pa.pa_sw_cvolume_divide.restype = POINTER(pa_cvolume_struct)
_pa.pa_sw_cvolume_divide_scalar .restype = POINTER(pa_cvolume_struct)
_pa.pa_sw_volume_from_dB.restype = POINTER(pa_volume_t)
_pa.pa_sw_volume_to_dB.restype = c_double
_pa.pa_sw_volume_from_linear.restype = POINTER(pa_volume_t)
_pa.pa_sw_volume_to_linear.restype = c_double
_pa.pa_cvolume_remap.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_get_balance.restype = c_float
_pa.pa_cvolume_set_balance.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_get_fade.restype = c_float
_pa.pa_cvolume_set_fade.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_scale.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_scale_mask.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_set_position.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_get_position.restype = POINTER(pa_volume_t)
_pa.pa_cvolume_merge.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_inc.restype = POINTER(pa_cvolume_struct)
_pa.pa_cvolume_dec.restype = POINTER(pa_cvolume_struct)