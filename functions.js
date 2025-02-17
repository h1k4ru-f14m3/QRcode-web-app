import QrCreator from './node_modules/qr-creator/dist/qr-creator.es6.min.js';

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').addEventListener('click', function(event) {
        let qrcode = document.querySelector('#qrcode');
        qrcode.innerHTML = "";

        event.preventDefault();
        console.log(QrCreator);
        let data = document.querySelector('input').value;

        QrCreator.render({
            text: data,
            radius: 0.5,
            ecLevel: 'H',
            fill: '#000000',
            background: null,
            size: 200
        }, qrcode);
    });
});