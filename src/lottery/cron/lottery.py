import subprocess, requests, json

from datetime import (
    datetime, timezone, timedelta)
from django.conf import settings

from lottery.models import Lottery
from lottery.cardano.operations import (
    generate_minting_policy)


# Every Monday 00:00 UTC
def new_lottery():
    # Create directory for the new policy
    today = datetime.now(timezone.utc)
    policy_path = settings.POLICY_DIR + \
        today.strftime('%m_%d_%y')
    subprocess.run(['mkdir', '-p', policy_path])

    # Generate minting policy for the
    # ticket nfts of this lottery
    policyID = generate_minting_policy(policy_path)

    # Get lottery draw date
    offset = 6 - today.weekday()
    lottery_day = today + timedelta(days=offset)
    draw_date = datetime(
        lottery_day.year, lottery_day.month,
        lottery_day.day,
        hour=9, minute=0,
        second=0, microsecond=0,
        tzinfo=timezone.utc
    )

    # Create lottery object
    lottery = Lottery.objects.create(
        policy_id=policyID,
        draw_date=draw_date)


# Every Sunday 09:00 UTC
def draw_lottery():
    # Generate luckyfive number
    url = 'https://api.random.org/json-rpc/4/invoke'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'jsonrpc': '2.0',
        'method': 'generateSignedIntegerSequences',
        'params': {
            'apiKey': settings.LUCKYFIVE_API_KEY,
            'n': 1,
            'length': 5,
            'min': 0,
            'max': 9,
            'base': 10,
            'userData': 'LuckyFive Weekly Draw'
        },
        'id': 1
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers)
    status_code = response.status_code

    if status_code == 200:
        response_dict = json.loads(response.text)
        print('Successfuly generated random number')
        print(response_dict)
    else:
        print('Error generating random number')

    # Create LuckyFive object

    # Update luckyfive in lottery object

    # Draw lottery winners

    # Deactivate current lottery

    pass
