---
description: "온라인 셀러의 반복 고객 문의에 답변 초안을 매일 만들어 드리는 쿼릭 운영 보조 서비스 안내와 파일럿 신청 방법입니다."
title: 셀러 문의 답변 보조 (파일럿)
permalink: /seller/
---
스마트스토어·쿠팡 등에서 매일 비슷한 고객 문의에 답하느라 시간을 쓰는 셀러를 위한 서비스입니다.
쿼릭이 문의를 분류하고 답변 초안을 만들어 드리면, **보내는 것은 사장님이 확인한 뒤 직접** 합니다.

## 하는 일

1. **문의 분류:** 사장님이 보내 주신 문의 내용(복사·내보내기 파일)을 배송·교환·사용법·재고 등으로 나눕니다.
2. **답변 초안:** 상품 상세와 사장님 운영 규칙(교환 기준·배송일 등)을 근거로 답변 초안을 씁니다. 근거가 없는 내용은 지어내지 않고 "확인 필요"로 표시합니다.
3. **일일 보고:** 그날 문의 수, 많이 나온 질문, 상세페이지에 추가하면 문의가 줄어들 항목을 정리합니다.

## 하지 않는 일

- 사장님 계정에 로그인하거나 고객에게 직접 답장을 보내지 않습니다.
- 후기·판매량·할인을 만들어 쓰지 않습니다.
- 매출 증가나 시간 절감을 보장하지 않습니다. 파일럿 기간에 실제로 얼마나 도움이 되는지 함께 확인합니다.

## 가격

- **7일 파일럿:** 무료. 실제 문의 일부로 초안 품질을 먼저 확인하세요.
- **월 운영:** 490,000원(부가세 별도). 파일럿 후 계속할지는 사장님이 정합니다. 결제는 파일럿이 끝난 뒤에만 안내합니다.

## 파일럿 신청

아래를 적고 버튼을 누르면 메일 앱이 열립니다. 그 메일을 보내 주시면 신청이 완료됩니다. 이 페이지는 입력한 내용을 따로 저장하지 않습니다.

<form id="lead" style="display:grid;gap:10px;max-width:520px">
  <label>업체명 / 판매 채널<br><input id="biz" required style="width:100%" placeholder="예: 스마트스토어 생활용품"></label>
  <label>하루 문의 수(대략)<br><input id="cnt" style="width:100%" placeholder="예: 20건"></label>
  <label>가장 많이 받는 문의<br><textarea id="pain" rows="3" style="width:100%" placeholder="예: 배송 언제 와요, 교환 되나요"></textarea></label>
  <label>회신 받을 연락처<br><input id="ct" required style="width:100%" placeholder="이메일 또는 휴대폰"></label>
  <button type="submit">메일로 파일럿 신청하기</button>
</form>
<p id="leadMsg"></p>
<script>
document.getElementById('lead').addEventListener('submit', function (e) {
  e.preventDefault();
  var v = function (id) { return document.getElementById(id).value.trim(); };
  var body = '업체/채널: ' + v('biz') + '\n하루 문의 수: ' + v('cnt') + '\n많은 문의: ' + v('pain') + '\n연락처: ' + v('ct');
  location.href = 'mailto:{{ site.email }}?subject=' + encodeURIComponent('[셀러 문의 보조 파일럿 신청] ' + v('biz')) + '&body=' + encodeURIComponent(body);
  document.getElementById('leadMsg').textContent = '메일 앱이 열렸다면 그 메일을 보내 주셔야 신청이 완료됩니다. 메일 앱이 없으면 {{ site.email }} 로 위 내용을 보내 주세요.';
});
</script>

보내 주신 연락처는 파일럿 안내에만 쓰고, 자세한 내용은 [개인정보처리방침](/privacy/)을 따릅니다.
