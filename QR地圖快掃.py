
classroom_list=[range(8401,8408),range(8301,8315),range(8204,8217),range(8108,8121),range(7407,7411),range(7309,7322),range(7211,7224),range(7116,7131),range(6407,6411),range(6309,6320),range(6211,6222),range(6106,6111),[8408,8308,8210,8115,7413,7315,7217,6411,6313,6215,6116]]




for i in classroom_list:
    for j in i:
        with open('appendSomething.txt', 'a') as f:
            f.write(f'''
<div class="modal fade" id="LHPS-{j}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel"><strong>LHPS-{j}</strong></h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <img src="https://wlan-auth.kh.edu.tw/aruba/webpic/LHPS-{j}.png" class="rounded mx-auto d-block" width="80%">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
        ''')