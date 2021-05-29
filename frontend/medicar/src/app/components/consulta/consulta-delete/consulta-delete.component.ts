import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { ConsultaService } from '../consulta.service';
import { NotificationService } from 'src/app/util/notification.service';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  selector: 'app-consulta-delete',
  templateUrl: './consulta-delete.component.html',
  styleUrls: ['./consulta-delete.component.css']
})
export class ConsultaDeleteComponent implements OnInit {

  constructor(
    private dialogRef: MatDialogRef<ConsultaDeleteComponent>,
    private consultaService:ConsultaService,
    private notificationService: NotificationService,
    @Inject(MAT_DIALOG_DATA) private data: {consulta_id: number}
  ) { }

  onCancelClick():void{
    this.dialogRef.close();
  }

  onConfirmClick():void{
    this.consultaService.deleteConsultaById(this.data.consulta_id).subscribe(
      (result) => {
        this.notificationService.showSuccessMsg('Consulta deletada com sucesso.')
        this.dialogRef.close()
      }
    )
  }

  ngOnInit(): void {
  }

}
