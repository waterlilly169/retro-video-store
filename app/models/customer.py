from app import db
from datetime import datetime


class Customer(db.Model):

    sort_fields = ["name", "registered_at", "postal_code"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    postal_code = db.Column(db.String(50))
    registered_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    phone = db.Column(db.String(50))
    videos = db.relationship("Video", back_populates="customers", secondary="rentals")
    __tablename__ = "customers"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "postal_code": self.postal_code,
            "registered_at": self.registered_at
        }

    @classmethod
    def from_json(cls, request_body):

        return cls(
            name = str(request_body["name"]),
            postal_code = str(request_body["postal_code"]),
            phone = str(request_body["phone"])
        )

    @classmethod
    def validate_id(cls, id):
        try:
            int(id)
        except ValueError:
            return "", 400

        obj = cls.query.get(id)

        if not obj:
            return {
                "message": f"Customer {id} was not found"
            }, 404

    @classmethod
    def check_input_fields(cls, request_body):

        required_fields = ["name", "postal_code", "phone"]

        for field in required_fields:
            if field not in request_body:
                return { "details" : f"Request body must include {field}."}, 400

        if len(request_body["postal_code"]) > 50 or len(request_body["phone"]) > 50 or len(request_body["name"]) > 200:
            return {
                "details" : "Input length exceeds database capacity."
            }, 400

