import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { NotificationService } from 'src/app/util/notification.service';
import { Agenda } from '../agenda.model';
import { ConsultaCreate } from '../consulta-create.model';
import { ConsultaService } from '../consulta.service';
import { Especialidade } from '../especialidade.model';
import { Medico } from '../medico.model';

@Component({
  selector: 'app-consulta-create',
  templateUrl: './consulta-create.component.html',
  styleUrls: ['./consulta-create.component.css']
})
export class ConsultaCreateComponent implements OnInit {

  especialidades:Especialidade[] = []
  medicos:Medico[] = []
  agendas:Agenda[] = []
  horarios: string[] = []

  consultaForm:any = {
    especialidade_id:'',
    medico_id:'',
    agenda_id:'',
    hora:''
  }

  constructor(private dialogRef: MatDialogRef<ConsultaCreateComponent>,
              private consultaService:ConsultaService,
              private notificationService: NotificationService) { }

  ngOnInit(): void {
    this.consultaService.getEspecialidades().subscribe(
      (result) =>{
        this.especialidades= result
      }
    )
  }
  onCancelClick():void{
    this.dialogRef.close();
  }

  getMedicosByEspecialidade():void{
    this.medicos = []
    this.agendas = []
    this.horarios = []
    this.consultaService.getMedicosByEspecialidade(this.consultaForm.especialidade_id)
                        .subscribe(
                          (medicosList)=>{
                            this.medicos= medicosList
                          }
                          )
  }

  getMedicoAgendas():void {
    this.agendas = []
    this.horarios = []
    this.consultaService.getAgendas(this.consultaForm.medico_id)
                        .subscribe(
                          (agendasMedico) => {
                            this.agendas = agendasMedico
                          }
                        )
  }

  getAgendaHorarios():void{
    const agendaSelecionada = this.agendas.find((agenda)=>agenda.id===this.consultaForm.agenda_id)
    this.horarios = agendaSelecionada !== undefined? agendaSelecionada.horarios : [] 
  }

  createConsulta():void{
    const consulta:ConsultaCreate = {
      agenda_id: this.consultaForm.agenda_id,
      horario: this.consultaForm.hora
    }
    this.consultaService.createConsulta(consulta).subscribe(
      (consultaCriada)=>{
        this.notificationService.showSuccessMsg('Consulta criada com sucesso.')
        this.dialogRef.close()
      }
    )
  }
}
