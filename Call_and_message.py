from bandwidth.bandwidth_client import BandwidthClient

from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.messaging.exceptions.messaging_exception import MessagingException

from bandwidth.voice.models.create_call_request import CreateCallRequest
from bandwidth.voice.exceptions.api_error_exception import ApiErrorException
from bandwidth.voice.bxml.response import Response
from bandwidth.voice.bxml.verbs import *

from bandwidth.multifactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.multifactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema

from bandwidth.phonenumberlookup.controllers.api_controller import APIController, ApiResponse, APIException
from bandwidth.phonenumberlookup.models.order_request import OrderRequest

from bandwidth.webrtc.models.session import Session
from bandwidth.webrtc.models.participant import Participant
from bandwidth.webrtc.models.publish_permission_enum import PublishPermissionEnum

bandwidth_client = BandwidthClient(
    voice_basic_auth_user_name='username',
    voice_basic_auth_password='password',
    messaging_basic_auth_user_name='username',
    messaging_basic_auth_password='password',
    multi_factor_auth_basic_auth_user_name='username',
    multi_factor_auth_basic_auth_password='password',
    phone_number_lookup_basic_auth_user_name='username',
    phone_number_lookup_basic_auth_password='password',
    web_rtc_basic_auth_user_name='username',
    web_rtc_basic_auth_password='password'
)
account_id = "12345"
voice_client = bandwidth_client.voice_client.client

##Create phone call
body = CreateCallRequest()
body.mfrom = "+17777777777"
body.to = "+16666666666"
body.application_id = "3-d-4-b-5"
body.answer_url = "https://test.com"


class ApiErrorResponseException:
    pass


try:
    response = voice_client.create_call(account_id, body=body)
    print(response.body.call_id) #c-3f758f24-a59bb21e-4f23-4d62-afe9-53o2ls3o4saio4l
    print(response.status_code) #201
except ApiErrorResponseException as e:
    print(e.description) #Invalid from: must be an E164 telephone number
    print(e.response_code) #400

messaging_client = bandwidth_client.messaging_client.client

body = MessageRequest()
body.application_id = "1-d-b"
body.to = ["+17777777777"]
body.mfrom = "+18888888888"
body.text = "Greetings!"

try:
    response = messaging_client.create_message(account_id, body)
    print(response.body.id) #1570819529611mexbyfr7ugrouuxy
    print(response.status_code) #202
except MessagingException as e:
    print(e.description) #Your request could not be accepted.
    print(e.response_code) #400