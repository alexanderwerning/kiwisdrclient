# Copyright 2011, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


"""This file exports public symbols."""


from kiwisdrclient.mod_pywebsocket._stream_base import BadOperationException
from kiwisdrclient.mod_pywebsocket._stream_base import ConnectionTerminatedException
from kiwisdrclient.mod_pywebsocket._stream_base import InvalidFrameException
from kiwisdrclient.mod_pywebsocket._stream_base import InvalidUTF8Exception
from kiwisdrclient.mod_pywebsocket._stream_base import UnsupportedFrameException
from kiwisdrclient.mod_pywebsocket._stream_hixie75 import StreamHixie75
from kiwisdrclient.mod_pywebsocket._stream_hybi import Frame
from kiwisdrclient.mod_pywebsocket._stream_hybi import Stream
from kiwisdrclient.mod_pywebsocket._stream_hybi import StreamOptions

# These methods are intended to be used by WebSocket client developers to have
# their implementations receive broken data in tests.
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_close_frame
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_header
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_length_header
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_ping_frame
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_pong_frame
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_binary_frame
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_text_frame
from kiwisdrclient.mod_pywebsocket._stream_hybi import create_closing_handshake_body


# vi:sts=4 sw=4 et