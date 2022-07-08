from django.shortcuts import render
import dns
from dns import resolver
# Create your views here.
from .models  import Message


def verify_dns_view(requests):
    room_messages = Message.objects.all()

    if requests.method == 'POST':
        domain = str(requests.POST.get('body'))
        mx_record = str(dns.resolver.query(domain, "MX")[0])
        txt_record_spf = str(dns.resolver.query(domain, "TXT")[0])
        result = dns.resolver.query(domain, 'A')
        # resul = dns.resolver.query(domain, 'CNAME')

        message = Message.objects.create(
            body=mx_record,
            ip=result,
            cname=result,
            txt=txt_record_spf

        )
    context={"message":room_messages}
    return render(requests, 'profile.html', context)
# def room(requests,pk):
#     room=Room.objects.get(id=pk)
#     room_messages = room.message_set.all()
#     participants = room.participants.all()
#
#     if requests.method == 'POST':
#         message = Message.objects.create(
#             user=requests.user,
#             room=room,
#             body=requests.POST.get('body')
#         )
#         room.participants.add(requests.user)
#         return redirect('room', pk=room.id)
#     context = {'room': room, 'room_messages': room_messages,
#                'participants': participants}
#     return render(requests,'base/room.html',context)