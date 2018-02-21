$('#all_download_button').click(function (event) {
    event.preventDefault(); //ボタン本来の機能を停止させる関数

    /* チェックされていない */
    if ($('[name=check]').prop('checked') == false) {
        return;
    }

    /* 選択中のチェックボックスのvalue値を取得 */
    let files_path = []
    $('[name=check]:checked').each(function () {
        files_path.push($(this).val());
    });

    /* URLタグの生成 */
    let link = document.createElement('a');
    link.href = '/submission_form/download/zip/?';

    /* URLパラメータを追加 */
    for (let i = 0; i < files_path.length; i++) {
        link.href += 'mydata[]=' + files_path[i] + '&';
    }

    link.click();
});
