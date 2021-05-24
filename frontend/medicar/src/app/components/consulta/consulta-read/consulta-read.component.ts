import { Component, OnInit, } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

import { AuthService } from 'src/app/auth/auth.service';
import { NotificationService } from 'src/app/util/notification.service';
import { ConsultaCreateComponent } from '../consulta-create/consulta-create.component';
import { ConsultaItem } from '../consulta-item.model';
import { Consulta } from '../consulta.model';

import { ConsultaService } from '../consulta.service';


@Component({
  selector: 'app-consulta-read',
  templateUrl: './consulta-read.component.html',
  styleUrls: ['./consulta-read.component.css']
})
export class ConsultaReadComponent implements OnInit {
  consultas: ConsultaItem[] = []
  userFullname:string=""

  displayedColumns = ['especialidade', 'profissional','data','hora','action'];

  constructor(private authService: AuthService,
              private consultaService: ConsultaService,
              private matDialog: MatDialog,
              private notificationService: NotificationService) {}

  ngOnInit(){
    this.userFullname = this.authService.getUserName()
    this.getConsultasList()
  }

  private getConsultasList():void{
    this.consultaService.list().subscribe(
      (consultas)=>{
        this.consultas = consultas.map((consulta)=>this.consultaToItem(consulta)) 
      }
    )
  }

  private consultaToItem(consulta:Consulta):ConsultaItem{
    return {
              id: consulta.id,
              data: consulta.dia,
              especialidade: consulta.medico.especialidade.nome,
              hora: consulta.horario,
              profissional: consulta.medico.nome
           }
  }
  
  deletarConsulta(id:number){
    this.consultaService.deleteConsultaById(id).subscribe(
      (result) => {
        this.notificationService.showSuccessMsg('Consulta deletada com sucesso.')
        this.getConsultasList()
      }
    )
  }

  openConsultaCreateDialog():void{
    const dialogRef = this.matDialog.open(ConsultaCreateComponent)
    dialogRef.afterClosed().subscribe(
      (result)=>{
        this.getConsultasList()
      }
    )
  }
  
}
