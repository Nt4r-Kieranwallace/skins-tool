R4NT | V1.2.0  -  DEEP SPACE EDITION
====================================
ต้องลง:  pip install zstandard   (Pydroid3: Pip -> zstandard)

โฟลเดอร์ (มีแค่สองอัน สร้างให้เองตอนรันครั้งแรก):
  output_bytes/   ไฟล์ .bytes / .pkg.bytes
  output_xml/     ไฟล์ .xml

เมนู:
  [1] bytes -> xml   อ่านจาก output_bytes  ผลไป output_xml
                     (คลายบีบอัด zstd ก่อนแปลง)
  [2] xml -> bytes   อ่านจาก output_xml    ผลไป output_bytes
                     (ไม่บีบอัด)
  สั่งตรงได้:  python main.py decode   |   python main.py encode

กติกา:
  - สแกนทุกโฟลเดอร์ย่อย
  - .pkg.bytes แตก/บีบใน RAM (BytesIO) ชื่อเดิมคงไว้
  - แปลงได้ = ย้ายไปอีกโฟลเดอร์ / แปลงไม่ได้ = ลบ / โฟลเดอร์ว่าง = ลบ
  - ตั้งค่าใน config.json

Credit : R4NT | V1.2.0
