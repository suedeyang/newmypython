html1='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0" crossorigin="anonymous">
    </head>
<body>
<script>
    function copyEvent(id)
    {
        var str = document.getElementById(id);
        window.getSelection().selectAllChildren(str);
        document.execCommand("Copy")
    }
</script>
<div class='container'>
<!-- Optional JavaScript; choose one of the two! -->

<!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-p34f1UUtsS3wqzfto5wAAmdvj+osOnFyQFpp4Ua3gs/ZVWx6oOypYoCJhGGScy+8" crossorigin="anonymous"></script>

<!-- Button trigger modal -->
<button style="margin-top:30px" type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  <strong>按我-前往 
'''

html2='''  
GoogleClassroom 進行線上課程</strong>
</button>

<button style="margin-top:30px" type="button" class="btn btn-danger"  onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSfhWSN-zhgnheY-dHG3TaFgIm1ljz6Hd8b0yXUfeyC2OjA1GQ/viewform?usp=sf_link')"><strong><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
  <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
</svg> 課程錯誤回報</strong></button> 
<button style="margin-top:30px" type="button" class="btn btn-info" onclick="window.open('https://youtu.be/4kW5P_s3qiI')"><strong>🎥教學影片</strong></button> 

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id="staticBackdropLabel"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-alarm" viewBox="0 0 16 16">
  <path d="M8.5 5.5a.5.5 0 0 0-1 0v3.362l-1.429 2.38a.5.5 0 1 0 .858.515l1.5-2.5A.5.5 0 0 0 8.5 9V5.5z"/>
  <path d="M6.5 0a.5.5 0 0 0 0 1H7v1.07a7.001 7.001 0 0 0-3.273 12.474l-.602.602a.5.5 0 0 0 .707.708l.746-.746A6.97 6.97 0 0 0 8 16a6.97 6.97 0 0 0 3.422-.892l.746.746a.5.5 0 0 0 .707-.708l-.601-.602A7.001 7.001 0 0 0 9 2.07V1h.5a.5.5 0 0 0 0-1h-3zm1.038 3.018a6.093 6.093 0 0 1 .924 0 6 6 0 1 1-.924 0zM0 3.5c0 .753.333 1.429.86 1.887A8.035 8.035 0 0 1 4.387 1.86 2.5 2.5 0 0 0 0 3.5zM13.5 1c-.753 0-1.429.333-1.887.86a8.035 8.035 0 0 1 3.527 3.527A2.5 2.5 0 0 0 13.5 1z"/>
</svg><strong> 提醒您!!</strong></h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <ul>
            <li>進入GoogleClassroom請使用<strong>龍華國小帳號</strong></li>
            <li>點一下就可以複製<a href="javascript:void(0)" onclick="copyEvent('copy')"><strong id="copy">@mail.lhps.kh.edu.tw</strong></a></li>
            <li>按照功課表的時間，進入對應的課程</li>
            <li>手機、平板請安裝<a href="https://support.google.com/edu/classroom/answer/6118412?hl=zh-Hant&ref_topic=10308276" target=_blank>GoogleClassroom APP</a>與<a href="https://support.google.com/meet/answer/7291339?hl=zh-Hant&ref_topic=7306097&co=GENIE.Platform%3DiOS&oco=1" target=_blank>GoogleMeet APP</a></li>
        </ul>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" onclick="window.open('https://classroom.google.com/a/mail.lhps.kh.edu.tw/')">我知道了!</button>
      </div>
    </div>
  </div>
</div>
<p></p>
<img class="img-fluid rounded-2 border border-3" src="imgs/
'''

html3='''
.jpg">
</div>

</body>
</html>
'''

for i in range(1,7):
  for j in range(1,17):
    class_num=str(i)+str(j).zfill(2)
    file_name=class_num+".html"
    print(file_name)
    f = open(file_name,'w',encoding='UTF-8')
    f.write(html1+str(class_num)+html2+str(class_num)+html3)
    f.close()


